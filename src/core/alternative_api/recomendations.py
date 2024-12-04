import pandas as pd
import sklearn.metrics.pairwise as pw
import sqlite3
from core.mooner.models import Song, History
from core.mooner.serializers import SongListSerializer
from sklearn.preprocessing import StandardScaler
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
import logging

logging.basicConfig(level=logging.INFO)
db_path = 'src/db.sqlite3'
scaler = StandardScaler()

def load_data():
    try:
        db = sqlite3.connect(db_path)
        query_history = 'SELECT * FROM mooner_history'
        query_songs = 'SELECT * FROM mooner_song'
        query_artists_songs = 'SELECT * FROM mooner_song_artists'
        query_artists = 'SELECT * FROM usuario_artist'

        history = pd.read_sql(sql=query_history, con=db)
        songs = pd.read_sql(sql=query_songs, con=db)
        artists = pd.read_sql(sql=query_artists, con=db)
        artists_songs = pd.read_sql(sql=query_artists_songs, con=db)

        db.close()
        return history, songs, artists_songs, artists
    except sqlite3.OperationalError as e:
        logging.error(f"Erro ao conectar ao banco de dados: {e}")
        return [], [], [], []


class RecomendationView(APIView):
    def get(self, request, user):
        history, songs, artists_songs, artists = load_data()

        try:
            user_history = History.objects.filter(usuario=user)
            if not user_history.exists():
                return Response(status=status.HTTP_200_OK, data={'recommended_songs': []})
        except History.DoesNotExist:
            return Response(status=status.HTTP_200_OK, data={'recommended_songs': []})

        logging.info(f"User history loaded for user: {user}")

        try:
            artists_songs_df = artists_songs.merge(songs, left_on='song_id', right_on='id', how='left')
            final_df = artists_songs_df.merge(artists, left_on='artist_id', right_on='user_id', how='left')
            final_df.rename(columns={'artistic_name': 'artist_name'}, inplace=True)


            logging.info(f'Table: {final_df.columns}')

            user_history = history[history['usuario_id'] == user]
            get_user_songs = user_history['song_id'].unique()

            logging.info(f"User songs: {get_user_songs}")

            user_songs = final_df[final_df['song_id'].isin(get_user_songs)]
            user_genres = user_songs['genre_id'].unique()
            user_artists = user_songs['artist_name'].unique()

            logging.info(f"User genres: {user_genres}")
            logging.info(f"User artists: {user_artists}")

            artist_frequencies = user_songs['artist_name'].value_counts().to_dict()
            genre_frequencies = user_songs['genre_id'].value_counts().to_dict()

            logging.info(f"Artist frequencies: {artist_frequencies}")
            logging.info(f"Genre frequencies: {genre_frequencies}")

            final_df['prioridade'] = (
                final_df['artist_name'].apply(lambda x: artist_frequencies.get(x, 0)) +
                final_df['genre_id'].apply(lambda x: genre_frequencies.get(x, 0))
            )

            logging.info(f"Filtrando músicas com base em gêneros {user_genres} e artistas {user_artists}")

            songs_filtered = final_df[
                (final_df['genre_id'].isin(user_genres)) |
                (final_df['artist_name'].isin(user_artists))
            ]

            logging.info(f"Songs filtered (first 10): {songs_filtered.head(10)}")

            if songs_filtered.empty:
                return Response(status=status.HTTP_204_NO_CONTENT, data={'msg': 'No songs found after filtering.'})

            # Seleciona apenas as colunas numéricas
            feature_columns = songs_filtered.select_dtypes(include=[float, int]).columns.difference([
                'id', 'title', 'cover_id', 'player_id', 'reproductions', 'artists',
                'song_id', 'artist_id', 'date_realized', 'uploaded_on', 'lyrics', 'prioridade'
            ])

            songs_filtered[feature_columns] = songs_filtered[feature_columns].fillna(0)

            priority_weight = 1.5
            songs_filtered.loc[:, feature_columns] = songs_filtered[feature_columns].mul(
                1 + songs_filtered['prioridade'] * (priority_weight - 1), axis=0
            )

            song_features = songs_filtered[feature_columns].values

            if song_features.shape[0] == 0:
                return Response(status=status.HTTP_204_NO_CONTENT, data={'msg': 'No song features found for recommendation.'})

            scaled_song_features = scaler.fit_transform(song_features)
            similarity = pw.cosine_similarity(scaled_song_features)

            history_indices = songs_filtered[songs_filtered['song_id'].isin(get_user_songs)].index.tolist()
            similarity_songs = []

            top_n = 10
            for song_i in history_indices:
                if song_i < similarity.shape[0]:
                    similarity_scores = list(enumerate(similarity[song_i]))
                    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
                    for i in similarity_scores[1:top_n+1]:
                        if i[0] < len(songs):
                            similarity_songs.append(songs.iloc[i[0]]['id'])

            similarity_songs = list(dict.fromkeys(similarity_songs))
            similar_songs_df = final_df[
                (final_df['song_id'].isin(similarity_songs)) &
                (~final_df['song_id'].isin(get_user_songs))
            ][['id_x', 'title']]

            recommended_songs = []
            for _, song in similar_songs_df.iterrows():
                recommended_songs.extend(Song.objects.filter(title=song['title']))

            serializer = SongListSerializer(recommended_songs[:6], many=True)

            logging.info(f"Recommended songs: {serializer.data}")

            return Response(status=status.HTTP_200_OK, data={'recommended_songs': serializer.data})
        except Exception as e:
            logging.error(f"Error processing request: {e}")
            return Response(status=status.HTTP_200_OK, data={"recommended_songs": []})

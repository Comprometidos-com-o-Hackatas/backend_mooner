from core.usuario.models import Artist
from core.uploader.models import Document, Image
from core.mooner.models import Genre, Song
from core.django_populate.infra.datas.song import songs

def Populate_songs():
    try:
        for data_songs in songs:
            add_artist_arr = set()
            for artists_data in data_songs['artists']:
                artists = Artist.objects.get(artistic_name=artists_data)
                add_artist_arr.add(artists)
            document = Document.objects.get(description=data_songs['player'])
            image = Image.objects.get(description=data_songs['cover'])
            genre = Genre.objects.get(description=data_songs['genre'])

            song = Song.objects.create(
                title=data_songs['title'],
                player=document,
                cover=image,
                genre=genre,
                lyrics=data_songs['lyrics'],
                background_light_color=data_songs['light_color'],
                background_dark_color=data_songs['dark_color'],
            )
            song.artists.set(add_artist_arr)
            print('musica populada', song)
            song.save()
    except Exception as e:
        print(e)
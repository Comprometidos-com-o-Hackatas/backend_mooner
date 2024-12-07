from core.usuario.models import Artist
from core.uploader.models import Image
from core.mooner.models import Song, Album
from core.django_populate.infra.datas.albuns import albuns

def Populate_albums():
    try:
        for album_data in albuns:
            add_songs_arr = set()
            for songs_data in album_data['songs']:
                song = Song.objects.get(title=songs_data)
                add_songs_arr.add(song)
            image = Image.objects.get(description=album_data['cover'])
            autor = Artist.objects.get(artistic_name=album_data['autor'])

            album = Album.objects.create(
                name=album_data['name'],
                autor=autor,
                cover=image,
                date_realized=album_data['date_realized'],
                background_light_color=album_data['light_color'],
                background_dark_color=album_data['dark_color'],
            )
            album.songs.set(add_songs_arr)
            print('Album populada', album)
            album.save()
    except Exception as e:
        print(e)
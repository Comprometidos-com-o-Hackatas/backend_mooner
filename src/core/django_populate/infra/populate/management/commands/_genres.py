from core.mooner.models import Genre
from core.django_populate.infra.datas.genres import genres

def Populate_genre():
    try:
        for genre_data in genres:
            genre = Genre.objects.create(**genre_data)
            genre.save()
    except Exception as e:
        print(e)
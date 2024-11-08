from core.django_populate.infra.datas.artists import artist
from core.usuario.models import Artist, Usuario

def Artist_Populate():
    try:
        for data_artist in artist:
            user = Usuario.objects.get(email=data_artist['user'])
            artists = Artist.objects.create(
                user=user,
                artistic_name=data_artist['artistic_name']
            )
            artists.save()
    except Exception as e:
        print(e)
    

from core.django_populate.infra.datas.users import users
from django.contrib.auth.hashers import make_password
from core.usuario.models import Usuario
from core.uploader.models import Image

def Populate_Users():
    if Usuario.objects.exists():
        return
    
    for user_data in users:
        try:
            perfil = Image.objects.get(description=user_data['perfil'])
            background = Image.objects.get(description=user_data['background'])

            user = Usuario.objects.create(
                email=user_data['email'],
                password=make_password(user_data['password']),
                is_superuser=user_data['is_superuser'],
                is_staff=user_data['is_staff'],
                is_active=user_data['is_active'],
                is_artist=user_data['is_artist'],
                perfil=perfil,
                background_image=background,
                background_light_color=user_data['light_color'],
                background_dark_color=user_data['dark_color'],
                description=user_data['description'],
            )
            user.save()
        except Exception as e:
            print(e)

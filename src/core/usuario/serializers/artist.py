from rest_framework.serializers import ModelSerializer, SlugRelatedField
from ..models import Usuario as User
from ..models import Artist


class UsuarioSeriazlier(ModelSerializer):
    class Meta:
        model = User
        fields = [
            "email",
            "first_name",
            "last_name",
            "is_active",
            "is_artist",
            "date_joined",
<<<<<<< HEAD
            "perfil",
            "background_image",
            "background_dark_color",
            "background_light_color",
            "description"
=======
            "perfil",  # Inclua este campo se o perfil estiver relacionado
            "background_light_color",
            "background_dark_color"
>>>>>>> bfd4600 (FEAT: Fixed things)
        ]
        depth = 2

class ArtistSerializer(ModelSerializer):
    # user = SlugRelatedField(slug_field="email", queryset=User.objects.all())
    user = UsuarioSeriazlier()
    class Meta:
        model = Artist
        fields = '__all__'
        depth = 2

class ArtistCreateSerializer(ModelSerializer):
    user = SlugRelatedField(slug_field="email", queryset=User.objects.all())
    class Meta:
        model = Artist
        fields = '__all__'
        depth = 2


        
    
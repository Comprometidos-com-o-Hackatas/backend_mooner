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
            "perfil",  # Inclua este campo se o perfil estiver relacionado
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


        
    
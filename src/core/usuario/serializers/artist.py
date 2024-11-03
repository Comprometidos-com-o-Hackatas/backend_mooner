from rest_framework.serializers import ModelSerializer, SlugRelatedField
from ..models import Usuario as User
from ..models import Artist

class ArtistSerializer(ModelSerializer):
    user = SlugRelatedField(slug_field="email", queryset=User.objects.all())
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


        
    
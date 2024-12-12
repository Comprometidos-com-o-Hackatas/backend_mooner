from rest_framework.serializers import ModelSerializer, SlugRelatedField
from ..models import Usuario as User
from ..models import Artist

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        depth=2
        
class ArtistSerializer(ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Artist
        fields = '__all__'
        depth = 2

class ArtistCreateSerializer(ModelSerializer):
    user = SlugRelatedField(slug_field="email", queryset=User.objects.all())
    class Meta:
        model = Artist
        fields = '__all__'


        
    
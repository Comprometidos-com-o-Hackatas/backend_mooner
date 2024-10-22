from rest_framework.serializers import ModelSerializer, SlugRelatedField
from ..models import Usuario as User
from ..models import Artist

class ArtistSerializer(ModelSerializer):
    user = SlugRelatedField(slug_field="email", queryset=User.objects.all())
    class Meta:
        model = Artist
        fields = '__all__'
        depth = 1

class ArtistCreateSerializer(ModelSerializer):
    user = SlugRelatedField(slug_field="email", queryset=User.objects.all())

    class Meta:
        model = Artist
        fields = '__all__'

    def create(self, validated_data):
   
        user_data = validated_data.pop('user')

        user = User.objects.get(email=user_data)

        artist = Artist.objects.create(user=user, **validated_data)

        return artist


        
    
from ..models import CommunityPosts
from core.usuario.models import Artist, Usuario
from rest_framework import serializers
from core.uploader.models import Image

class PerfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'

class UserSerializers(serializers.ModelSerializer):
    perfil = PerfilSerializer()
    class Meta:
        model = Usuario
        fields = '__all__'

class ArtistUserSerializer(serializers.ModelSerializer):
    user = UserSerializers()
    class Meta:
        model = Artist
        fields = '__all__'

class CommunityPostsSerializer(serializers.ModelSerializer):
    autor = ArtistUserSerializer()
    class Meta:
        model = CommunityPosts
        fields = '__all__'
        depth = 3

class CommunityPostsCreateSerializer(serializers.ModelSerializer):
    autor = serializers.SlugRelatedField(
        slug_field='artistic_name',
        queryset=Artist.objects.all()
    )
    class Meta:
        model = CommunityPosts
        fields = '__all__'
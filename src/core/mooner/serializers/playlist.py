from ..models import Playlist
from core.usuario.models import Usuario
from core.uploader.models import Image
from core.mooner.models import Song
from rest_framework import serializers

class PlaylistCreateSerializer(serializers.ModelSerializer):
    owners = serializers.PrimaryKeyRelatedField(queryset=Usuario.objects.all(), many=True)
    songs = serializers.PrimaryKeyRelatedField(queryset=Song.objects.all(), many=True) 
    # cover = serializers.SlugRelatedField(slug_field=;) # Definindo o campo
    class Meta:
        model = Playlist
        fields = ['name', 'songs', 'owners']

class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = ['id', 'name', 'songs', 'owners', 'cover']
        depth = 2

    
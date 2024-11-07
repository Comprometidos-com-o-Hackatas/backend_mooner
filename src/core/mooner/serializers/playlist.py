from ..models import Playlist
from core.usuario.models import Usuario
from rest_framework import serializers

class PlaylistCreateSerializer(serializers.ModelSerializer):
    owners = serializers.PrimaryKeyRelatedField(queryset=Usuario.objects.all(), many=True)  # Definindo o campo
    class Meta:
        model = Playlist
        fields = ['name', 'songs', 'owners']

class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = ['name', 'songs', 'owners']
        depth = 2

    
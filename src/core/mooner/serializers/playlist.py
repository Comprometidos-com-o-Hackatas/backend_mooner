from ..models import Playlist, Song
from core.usuario.models import Usuario

from rest_framework import serializers

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'

class PlaylistSerializer(serializers.ModelSerializer):
    owners = UsuarioSerializer(many=True)
    songs = SongSerializer(many=True)

    class Meta:
        model = Playlist
        fields = '__all__'
        depth = 2
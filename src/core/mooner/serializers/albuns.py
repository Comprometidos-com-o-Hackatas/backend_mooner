from ..models import Album, Song
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

class AlbumSerializer(serializers.ModelSerializer):
    songs = SongSerializer(many=True)
    autors = UsuarioSerializer(many=True)

    class Meta:
        model = Album
        fields = '__all__'
        depth = 2
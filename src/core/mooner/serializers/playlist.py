from ..models import Playlist, Song
from core.usuario.models import Usuario

from rest_framework import serializers

class PlaylistSerializer(serializers.ModelSerializer):
    owners = serializers.PrimaryKeyRelatedField(many=True, queryset=Usuario.objects.all())
    songs = serializers.PrimaryKeyRelatedField(many=True, queryset=Song.objects.all())

    class Meta:
        model = Playlist
        fields = '__all__'
        depth = 1 
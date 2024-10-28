from ..models import LikedSong
from rest_framework import serializers

class LikedSongSerializer(serializers.ModelSerializer):

    class Meta:
        model = LikedSong
        fields = '__all__'
        depth = 2
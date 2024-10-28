from ..models import CommunityPosts, Song, Community
from rest_framework import serializers

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'

class CommunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Community
        fields = '__all__'

class CommunityPostsSerializer(serializers.ModelSerializer):
    songs = SongSerializer(many=True)

    class Meta:
        model = CommunityPosts
        fields = '__all__'
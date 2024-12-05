from ..models import CommunityPosts
from rest_framework import serializers

class CommunityPostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommunityPosts
        fields = '__all__'
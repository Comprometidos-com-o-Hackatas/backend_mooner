from ..models import Following
from rest_framework import serializers

class FollowingCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Following
        fields = '__all__'

class FollowingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Following
        fields = '__all__'
        depth = 2

from ..models import Following
from rest_framework import serializers


class FollowingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Following
        fields = '__all__'
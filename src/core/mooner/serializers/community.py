from ..models import Community
from rest_framework import serializers
from core.uploader.models import Image


class CommunityCreateSerializer(serializers.ModelSerializer):
    cover = serializers.SlugRelatedField(
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
    class Meta:
        model = Community
        fields = '__all__'

class CommunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Community
        fields = '__all__'
        depth=2




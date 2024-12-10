from ..models import Community
from rest_framework import serializers
from core.uploader.models import Image
from core.usuario.models import Artist


class CommunityCreateSerializer(serializers.ModelSerializer):
    cover = serializers.SlugRelatedField(
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
    autor = serializers.SlugRelatedField(
        queryset=Artist.objects.all(),
        slug_field="artistic_name",
    )
    class Meta:
        model = Community
        fields = '__all__'

class CommunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Community
        fields = '__all__'
        depth=2




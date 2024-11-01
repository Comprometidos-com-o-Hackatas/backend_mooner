from ..models import Album, Song
from core.usuario.models import Artist
from core.uploader.models import Image
from rest_framework import serializers


class AlbumCreateSerializer(serializers.ModelSerializer):
    autor = serializers.PrimaryKeyRelatedField(queryset=Artist.objects.all())
    cover = serializers.SlugRelatedField(
        queryset=Image.objects.all(),
        slug_field="attachment_key",
    )
    class Meta:
        model = Album
        fields = '__all__'

class AlbumSerializer(serializers.ModelSerializer):
    autor = serializers.PrimaryKeyRelatedField(queryset=Artist.objects.all())
    cover = serializers.SlugRelatedField(
        queryset=Image.objects.all(),
        slug_field="attachment_key",
    )
    class Meta:
        model = Album
        fields = "__all__"
        depth = 2
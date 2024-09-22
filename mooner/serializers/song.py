from ..models import Song
from rest_framework import serializers
from uploader.serializers import ImageSerializer
from uploader.models import Image

class SongSerializer(serializers.ModelSerializer):
    cover_attachment_key = serializers.SlugRelatedField(
        source="cover",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
    cover = ImageSerializer(
        required=False,
        read_only=True
    )
    class Meta:
        model = Song
        fields = '__all__'
        depth = 2

class SongListSerializer(serializers.ModelField):
    cover_attachment_key = serializers.SlugRelatedField(
        source="cover",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
    cover = ImageSerializer(
        required=False,
        read_only=True
    )
    class Meta:
        model = Song
        fields = '__all__'



        
    
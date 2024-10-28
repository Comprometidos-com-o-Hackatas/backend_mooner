from ..models import Song, Genre
from rest_framework import serializers
from core.uploader.serializers import ImageSerializer, DocumentSerializer
from core.uploader.models import Image, Document
from core.usuario.models import Artist

class SongDetailSerializer(serializers.ModelSerializer):
    cover = ImageSerializer(required=False)
    document = DocumentSerializer(required=False)
    class Meta:
        model = Song
        fields = '__all__'
        depth = 2

class SongListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'
        depth = 1

class SongSerializer(serializers.ModelSerializer):
    genre = serializers.SlugRelatedField(slug_field='description', queryset=Genre.objects.all())
    cover = serializers.SlugRelatedField(
        queryset=Image.objects.all(),
        slug_field="attachment_key",
    )
    player = serializers.SlugRelatedField(
        queryset=Document.objects.all(),
        slug_field="attachment_key",
    )
    class Meta:
        model = Song
        fields = '__all__'


        





        
    
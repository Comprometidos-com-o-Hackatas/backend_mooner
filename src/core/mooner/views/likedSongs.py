from ..serializers import LikedSongSerializer
from ..models import LikedSong
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from utils.likedSong_filter import LikedSongFilter

class LikedSongsViewSet(ModelViewSet):
    queryset = LikedSong.objects.all()
    serializer_class = LikedSongSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = LikedSongFilter

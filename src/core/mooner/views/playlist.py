from ..models import Playlist
from ..serializers import PlaylistSerializer
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from utils.playlist_filter import PlaylistFilter

class PlaylistViewSet(ModelViewSet):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = PlaylistFilter
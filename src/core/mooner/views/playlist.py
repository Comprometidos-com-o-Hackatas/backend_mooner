from ..models import Playlist
from ..serializers import PlaylistSerializer, PlaylistCreateSerializer
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from utils.playlist_filter import PlaylistFilter

class PlaylistViewSet(ModelViewSet):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = PlaylistFilter

    def get_serializer_class(self):
        if self.action == 'create':
            return PlaylistCreateSerializer
        return PlaylistSerializer
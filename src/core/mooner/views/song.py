from ..serializers import SongSerializer, SongDetailSerializer, SongListSerializer
from ..models import Song
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from utils.song_filter import SongFilters

class SongViewSet(ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = SongFilters

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return SongDetailSerializer
        elif self.action == 'list':
            return SongListSerializer
        return SongSerializer

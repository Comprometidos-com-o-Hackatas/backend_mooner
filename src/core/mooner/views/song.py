from ..serializers import SongSerializer, SongDetailSerializer, SongListSerializer
from ..models import Song
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from utils.song_filter import SongFilter

class SongViewSet(ModelViewSet):
    queryset = Song.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = SongFilter

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return SongDetailSerializer
        elif self.action == 'list':
            return SongListSerializer
        return SongSerializer

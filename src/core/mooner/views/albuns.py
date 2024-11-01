from ..serializers import AlbumSerializer,AlbumCreateSerializer
from ..models import Album
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from utils.albuns_filter import AlbumFilter

class AlbumViewSet(ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = AlbumFilter

    def get_serializer_class(self):
        if self.action == 'create':
            return AlbumCreateSerializer
        return AlbumSerializer

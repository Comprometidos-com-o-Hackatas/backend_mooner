from ..models import Album
from ..serializers import AlbumSerializer
from rest_framework.viewsets import ModelViewSet

class AlbumViewSet(ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

    http_method_names = ["get", "post", "put", "delete"]
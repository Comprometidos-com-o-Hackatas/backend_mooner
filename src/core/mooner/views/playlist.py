from ..models import Playlist
from ..serializers import PlaylistSerializer
from rest_framework.viewsets import ModelViewSet

class PlaylistViewSet(ModelViewSet):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
from ..serializers import SongSerializer
from ..models import Song
from rest_framework.viewsets import ModelViewSet

class SongViewSet(ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

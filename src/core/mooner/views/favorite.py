from rest_framework.viewsets import ModelViewSet

from ..models import Favorite
from ..serializers import FavoriteSerializer

class FavoriteViewSet(ModelViewSet):
    queryset = Favorite
    serializer_class = FavoriteSerializer
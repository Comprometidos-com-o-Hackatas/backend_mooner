from rest_framework.viewsets import ModelViewSet

from ..models import Favorite
from ..serializers import FavoriteSerializer

class FavoriteViewSet(ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer

    http_method_names = ["get", "post", "put", "delete"]
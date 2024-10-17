from ..models import Genre
from ..serializers import GenreSerializer
from rest_framework.viewsets import ModelViewSet

class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

    http_method_names = ["get", "post", "put", "delete"]
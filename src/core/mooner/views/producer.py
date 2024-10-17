from ..serializers import ProducerSerializer
from ..models import Producer
from rest_framework.viewsets import ModelViewSet

class ProducerViewSet(ModelViewSet):
    queryset = Producer.objects.all()
    serializer_class = ProducerSerializer

    http_method_names = ["get", "post", "put", "delete"]
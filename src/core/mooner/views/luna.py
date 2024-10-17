from ..models import LunaAI
from ..serializers import LunaAISerializer
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend 

class LunaAIViewSet(ModelViewSet):
    queryset = LunaAI.objects.all().order_by('-id')
    serializer_class = LunaAISerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('usuario', )

    http_method_names = ["get", "post"]

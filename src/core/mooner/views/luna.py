from ..models import LunaAI
from ..serializers import LunaAISerializer
from rest_framework.viewsets import ModelViewSet

class LunaAIViewSet(ModelViewSet):
    queryset = LunaAI.objects.all()
    serializer_class = LunaAISerializer
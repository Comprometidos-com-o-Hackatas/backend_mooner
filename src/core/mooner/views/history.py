from ..models import History
from ..serializers import HistorySerializer, CreateHistorySerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from utils.history_filter import HistoryFilter

class HistoryViewSet(ModelViewSet):
    queryset = History.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = HistoryFilter
    
    http_method_names = ["get", "post", "put", "delete"]

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateHistorySerializer
        return HistorySerializer


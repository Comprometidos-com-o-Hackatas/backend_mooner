from ..models import History
from rest_framework.serializers import ModelSerializer

class CreateHistorySerializer(ModelSerializer):
    class Meta:
        model = History
        fields = '__all__'

class HistorySerializer(ModelSerializer):
    class Meta:
        model = History
        fields = '__all__'
        depth = 2
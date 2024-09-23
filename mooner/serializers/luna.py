from ..models import LunaAI
from rest_framework import serializers

class LunaAISerializer(serializers.ModelSerializer):
    class Meta:
        model = LunaAI
        fields = '__all__'


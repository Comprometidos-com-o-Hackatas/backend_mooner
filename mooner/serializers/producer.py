from ..models import Producer
from rest_framework import serializers 

class ProducerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producer
        fields = '__all__'

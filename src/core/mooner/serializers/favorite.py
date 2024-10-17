from ..models import Favorite
from rest_framework import serializers

class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'
        depth = 1
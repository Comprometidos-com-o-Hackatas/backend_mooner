from core.mooner.models import CommunityUsers
from rest_framework.serializers import ModelSerializer

class CommunityUsersCreateSerializers(ModelSerializer):
    class Meta:
        model = CommunityUsers
        fields = '__all__'

class CommunityUsersSerializers(ModelSerializer):
    class Meta:
        model = CommunityUsers
        fields = '__all__'
        detph = 2
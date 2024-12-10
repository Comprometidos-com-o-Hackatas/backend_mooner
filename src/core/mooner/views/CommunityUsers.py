from core.mooner.models import CommunityUsers
from core.mooner.serializers import CommunityUsersCreateSerializers, CommunityUsersSerializers
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from utils.communityUsers_filter import CommunityUsersFilter

class CommunityUsersViewSet(ModelViewSet):
    queryset = CommunityUsers.objects.all()
    serializer_class = CommunityUsersSerializers
    filter_backends = [DjangoFilterBackend]
    filterset_class = CommunityUsersFilter

    def get_serializer_class(self):
        if self.action == 'create':
            return CommunityUsersCreateSerializers
        return CommunityUsersSerializers

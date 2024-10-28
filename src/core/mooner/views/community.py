from ..serializers import CommunitySerializer
from ..models import Community
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from utils.community_filter import CommunityFilter

class CommunityViewSet(ModelViewSet):
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = CommunityFilter

from ..serializers import FollowingSerializer
from ..models import Following
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from utils.following_filter import FollowingFilter

class FollowingViewSet(ModelViewSet):
    queryset = Following.objects.all()
    serializer_class = FollowingSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = FollowingFilter
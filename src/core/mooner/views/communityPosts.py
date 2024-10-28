from ..serializers import CommunityPostsSerializer
from ..models import CommunityPosts
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from utils.communityPosts_filter import CommunityPostsFilter

class CommunityPostsViewSet(ModelViewSet):
    queryset = CommunityPosts.objects.all()
    serializer_class = CommunityPostsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = CommunityPostsFilter

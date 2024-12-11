from ..serializers import CommunityPostsSerializer, CommunityPostsCreateSerializer
from ..models import CommunityPosts
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from utils.communityPosts_filter import CommunityPostsFilter
from rest_framework.response import Response
from rest_framework import status

class CommunityPostsViewSet(ModelViewSet):
    queryset = CommunityPosts.objects.all()
    serializer_class = CommunityPostsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = CommunityPostsFilter

    def get_serializer_class(self):
        if self.action == 'create':
            return CommunityPostsCreateSerializer
        return CommunityPostsSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        serialized_response = CommunityPostsSerializer(serializer.instance)
        headers = self.get_success_headers(serialized_response.data)
        
        return Response(serialized_response.data, status=status.HTTP_201_CREATED, headers=headers)

import django_filters
from core.mooner.models import CommunityPosts, Community

class CommunityPostsFilter(django_filters.FilterSet):
    autor_email = django_filters.BaseInFilter(field_name='autor__id', lookup_expr='in')
    community_id = django_filters.NumberFilter(field_name='community__id', lookup_expr='exact')

    class Meta:
        model = CommunityPosts
        fields = ['autor_id', 'community_id']  

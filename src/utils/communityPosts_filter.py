import django_filters
from core.mooner.models import CommunityPosts

class CommunityPostsFilter(django_filters.FilterSet):
    autor = django_filters.BaseInFilter(field_name='autor', lookup_expr='in')
    title = django_filters.BaseInFilter(field_name='title', lookup_expr='in')

    class Meta:
        model = CommunityPosts
        fields = ['autor', 'title']  

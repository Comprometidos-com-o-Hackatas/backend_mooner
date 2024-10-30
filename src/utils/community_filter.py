import django_filters
from core.mooner.models import Community

class CommunityFilter(django_filters.FilterSet):
    autor_id = django_filters.NumberFilter(field_name='autor__id', lookup_expr='exact')

    class Meta:
        model = Community
        fields = ['autor_id']  

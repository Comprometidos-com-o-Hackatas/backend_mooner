import django_filters
from core.mooner.models import Community

class CommunityFilter(django_filters.FilterSet):
    autor = django_filters.BaseInFilter(field_name='autor', lookup_expr='in')
    name = django_filters.BaseInFilter(field_name='name', lookup_expr='in')

    class Meta:
        model = Community
        fields = ['autor', 'name']  

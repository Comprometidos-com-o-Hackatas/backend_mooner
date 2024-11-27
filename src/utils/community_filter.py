import django_filters
from core.mooner.models import Community

class CommunityFilter(django_filters.FilterSet):
    autor_email = django_filters.BaseInFilter(field_name='autor__email', lookup_expr='in')

    class Meta:
        model = Community
        fields = ['autor_email']  

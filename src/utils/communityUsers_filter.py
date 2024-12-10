import django_filters
from core.mooner.models import CommunityUsers

class CommunityUsersFilter(django_filters.FilterSet):
    user_email = django_filters.BaseInFilter(field_name='user__email', lookup_expr='in')
    community_id = django_filters.NumberFilter(field_name='community__id', lookup_expr='exact')

    class Meta:
        model = CommunityUsers
        fields = ['user_email', 'community_id']  

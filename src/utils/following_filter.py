import django_filters
from core.mooner.models import Following

class FollowingFilter(django_filters.FilterSet):
    user_id = django_filters.BaseInFilter(field_name='user__id', lookup_expr='in')
    artist_id = django_filters.BaseInFilter(field_name='artist__id', lookup_expr='in')

    class Meta:
        model = Following
        fields = ['artist_id', 'user_id']  

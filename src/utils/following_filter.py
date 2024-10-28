import django_filters
from core.mooner.models import LikedSong

class FollowingFilter(django_filters.FilterSet):
    user = django_filters.BaseInFilter(field_name='user', lookup_expr='in')
    artist = django_filters.BaseInFilter(field_name='artist', lookup_expr='in')

    class Meta:
        model = LikedSong
        fields = ['artist', 'user']  

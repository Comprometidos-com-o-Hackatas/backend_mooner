import django_filters
from core.mooner.models import LikedSong

class LikedSongFilter(django_filters.FilterSet):
    song = django_filters.BaseInFilter(field_name='song', lookup_expr='in')
    user = django_filters.BaseInFilter(field_name='user', lookup_expr='in')

    class Meta:
        model = LikedSong
        fields = ['song', 'user']  

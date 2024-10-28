import django_filters
from core.mooner.models import Playlist

class PlaylistFilter(django_filters.FilterSet):
    song = django_filters.BaseInFilter(field_name='songs', lookup_expr='in')
    name = django_filters.BaseInFilter(field_name='name', lookup_expr='in')
    owner = django_filters.BaseInFilter(field_name='owners', lookup_expr='in')

    class Meta:
        model = Playlist
        fields = ['songs', 'name', 'owners']  

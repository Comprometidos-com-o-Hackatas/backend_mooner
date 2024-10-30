import django_filters
from core.mooner.models import Album

class AlbumFilter(django_filters.FilterSet):
    songs = django_filters.BaseInFilter(field_name='songs', lookup_expr='in')
    autor = django_filters.BaseInFilter(field_name='autor', lookup_expr='in')

    class Meta:
        model = Album
        fields = ['autor', 'songs']  

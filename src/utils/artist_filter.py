import django_filters
from core.usuario.models import Artist

class ArtistFilter(django_filters.FilterSet):
    artistic_name = django_filters.BaseInFilter(
        field_name='artistic_name', lookup_expr='in'
    )

    class Meta:
        model = Artist
        fields = ['artistic_name']  

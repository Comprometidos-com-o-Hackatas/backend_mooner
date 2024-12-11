import django_filters
from django.db.models import Q
from core.mooner.models import Song

class SongFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(method='get_title_or_artist')
    artists = django_filters.BaseInFilter(field_name='artists__artistic_name', lookup_expr='in')
    class Meta:
        model = Song
        fields = ['search']
    
    def get_title_or_artist(self, queryset, name, value):
        return queryset.filter(Q(title__icontains=value) | Q(artists__artistic_name__icontains=value) | Q(genre__description=value))


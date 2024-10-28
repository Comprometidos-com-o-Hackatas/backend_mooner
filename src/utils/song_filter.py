import django_filters
from django.db.models import Q
from core.mooner.models import Song

class SongFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(method='get_title_or_artist')

    class Meta:
        model = Song
        fields = ['search']
    
    def get_title_or_artist(self, queryset, name, value):
        return queryset.filter(Q(title=value) | Q(artists__artistic_name=value))


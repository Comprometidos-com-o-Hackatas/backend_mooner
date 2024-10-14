import django_filters
from core.mooner.models import History

class HistoryFilter(django_filters.FilterSet):
    song = django_filters.BaseInFilter(field_name='song', lookup_expr='in')
    class Meta:
        model = History
        fields = ['usuario', 'song']  

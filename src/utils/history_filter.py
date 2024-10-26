import django_filters
from core.mooner.models import History
from django.db.models import Q



class HistoryFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(method='search_in_history')

    class Meta:
        model = History
        fields = ['search']

    def search_in_history(self, queryset, name, value):
        return queryset.filter(Q(song__title=value) | Q(song__artists__artistic_name=value))


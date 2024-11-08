import django_filters
from core.uploader.models import Image
class ImagesFilter(django_filters.FilterSet):
    attachment_key = django_filters.BaseInFilter(field_name='attachment_key', lookup_expr='in')

    class Meta:
        model = Image
        fields = ['attachment_key']  

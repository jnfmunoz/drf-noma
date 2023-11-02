import django_filters
from asesora.models import Accidente

class AccidenteFilter(django_filters.FilterSet):
    tipo_accidente = django_filters.CharFilter(field_name='tipo_accidente__id', lookup_expr='icontains')

    class Meta:
        model = Accidente
        fields = ['tipo_accidente']

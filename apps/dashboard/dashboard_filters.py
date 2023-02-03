from apps.orcamentos.models import Orcamento
from django_filters import FilterSet, DateFromToRangeFilter
from bootstrap_datepicker_plus.widgets import DatePickerInput, TimePickerInput
from django import forms

class OrcamentosFilter(FilterSet):
    created = DateFromToRangeFilter()

    class Meta:
        model = Orcamento
        fields = ['created']


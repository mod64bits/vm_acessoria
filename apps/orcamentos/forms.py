from django.forms import ModelForm

from bootstrap_modal_forms.forms import BSModalModelForm
from bootstrap_datepicker_plus.widgets import DatePickerInput

from .models import Orcamento, ItemProduto, ItemMaoDeObra


class OrcamentoUpdateForm(ModelForm):
    class Meta:
        model = Orcamento
        fields = '__all__'
        widgets = {
            "validade": DatePickerInput(),

        }


class OrcamentoProdutoForm(BSModalModelForm):
    class Meta:
        model = ItemProduto
        exclude = ['orcamento']


class OrcamentoMaoDeObraForm(BSModalModelForm):
    class Meta:
        model = ItemMaoDeObra
        exclude = ['orcamento']

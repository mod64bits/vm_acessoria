from django.forms import ModelForm

from bootstrap_modal_forms.forms import BSModalModelForm
from bootstrap_datepicker_plus.widgets import DatePickerInput

from .models import Orcamento, ItemProduto


class OrcamentoUpdateForm(ModelForm):
    class Meta:
        model = Orcamento
        fields = '__all__'
        widgets = {
            "validade": DatePickerInput(),

        }




class OrcamentoProdutoForm(BSModalModelForm):
    # def __init__(self, *args, **kwargs):
    #     super(OrcamentoProdutoForm, self).__init__(*args, **kwargs)
    #     self.fields['orcamento'] = Form.
    print()
    class Meta:
        model = ItemProduto
        exclude = ['orcamento']

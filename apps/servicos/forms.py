from django.forms import ModelForm, Textarea
from .models import Servico, CategoriaServico
from bootstrap_modal_forms.forms import BSModalModelForm


class ServicoForm(BSModalModelForm):
    class Meta:
        model = Servico
        fields = '__all__'
        widgets = {
            "descricao": Textarea(attrs={"cols": 20, "rows": 5}),
        }


class CategoriaServicoForm(BSModalModelForm):
    class Meta:
        model = CategoriaServico
        fields = '__all__'


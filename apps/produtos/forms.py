from .models import Fornecedor, Categoria
from bootstrap_modal_forms.forms import BSModalModelForm


class FornecedorForm(BSModalModelForm):
    class Meta:
        model = Fornecedor
        fields = '__all__'


class CategoriaForm(BSModalModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'

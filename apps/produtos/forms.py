from django import forms

from .models import Fornecedor, Categoria, Produto
from bootstrap_modal_forms.forms import BSModalModelForm


class FornecedorForm(BSModalModelForm):
    class Meta:
        model = Fornecedor
        fields = '__all__'


class CategoriaForm(BSModalModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'


class ProdutoForm(BSModalModelForm):
    # def __init__(self, *args, **kwargs):
    #     super(ProdutoForm, self).__init__(*args, **kwargs)
    #
    #     for visible in self.visible_fields():
    #         if visible.field.widget.input_type == 'select':
    #             visible.field.widget.attrs['class'] = 'select2bs4'

    class Meta:
        model = Produto
        fields = '__all__'


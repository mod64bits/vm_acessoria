from django.urls import reverse_lazy
from .forms import FornecedorForm
from django.views.generic.list import ListView
from django.http import JsonResponse
from django.template.loader import render_to_string
from .models import Fornecedor
from bootstrap_modal_forms.generic import (
    BSModalCreateView,
    BSModalUpdateView,
    BSModalDeleteView,
    BSModalReadView
)


class FornecedorListView(ListView):
    model = Fornecedor
    template_name = 'produtos/fornecedor_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_open_fornecedores'] = True
        context['active_fornecedores'] = True
        return context


class FornecedorCreateView(BSModalCreateView):
    template_name = 'produtos/novo_fornecedor.html'
    form_class = FornecedorForm
    success_message = 'Success: Fornecedor Criado.'
    success_url = reverse_lazy('produtos:lista_fornecedor')


class FornecedorUpdateView(BSModalUpdateView):
    model = Fornecedor
    template_name = 'produtos/atualizar_fornecedor.html'
    form_class = FornecedorForm
    success_message = 'Success: Fornecedor Atualizado.'
    success_url = reverse_lazy('produtos:lista_fornecedor')


class FornecedorDeleteView(BSModalDeleteView):
    model = Fornecedor
    template_name = 'produtos/delete_fornecedor.html'
    success_message = 'Success: Fornecedor excluído com sucesso.'
    success_url = reverse_lazy('produtos:lista_fornecedor')

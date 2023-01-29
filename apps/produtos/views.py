from django.urls import reverse_lazy
from .forms import FornecedorForm, CategoriaForm, ProdutoForm
from django.views.generic.list import ListView
from django.http import JsonResponse
from django.template.loader import render_to_string
from .models import Fornecedor, Categoria, Produto
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
        context['menu_open_produto'] = True
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


class CategoriasListView(ListView):
    model = Categoria
    template_name = 'produtos/categoria_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_open_produto'] = True
        context['active_produto_categoria'] = True
        return context


class CategoriaCreateView(BSModalCreateView):
    template_name = 'produtos/nova_categoria.html'
    form_class = CategoriaForm
    success_message = 'Success: Categoria Criada.'
    success_url = reverse_lazy('produtos:lista_categorias')


class CategoriaUpdateView(BSModalUpdateView):
    model = Categoria
    template_name = 'produtos/atualizar_categoria.html'
    form_class = CategoriaForm
    success_message = 'Success: Categoria Atualizada.'
    success_url = reverse_lazy('produtos:lista_categorias')


class CategoriaDeleteView(BSModalDeleteView):
    model = Categoria
    template_name = 'produtos/delete_categoria.html'
    success_message = 'Success: Categoria excluída com sucesso.'
    success_url = reverse_lazy('produtos:lista_categorias')


class ProdutoListView(ListView):
    model = Produto
    template_name = 'produtos/produto_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_open_produto'] = True
        context['active_produto'] = True
        return context


class ProdutoCreateView(BSModalCreateView):
    template_name = 'produtos/novo_produto.html'
    form_class = ProdutoForm
    success_message = 'Success: Produto criado com sucesso.'
    success_url = reverse_lazy('produtos:lista_produto')


class ProdutoUpdateView(BSModalUpdateView):
    model = Produto
    template_name = 'produtos/atualizar_produto.html'
    form_class = ProdutoForm
    success_message = 'Success: Book was updated.'
    success_url = reverse_lazy('produtos:lista_produto')


class ProdutoDeleteView(BSModalDeleteView):
    model = Produto
    template_name = 'produtos/delete_produto.html'
    success_message = 'Success: Produto Deletado.'
    success_url = reverse_lazy('produtos:lista_produto')


class ProdutoReadView(BSModalReadView):
    model = Produto
    template_name = 'produtos/read_produto.html'

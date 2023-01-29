from django.urls import path

from .views import (FornecedorCreateView, FornecedorListView, FornecedorUpdateView, FornecedorDeleteView,
                    CategoriaCreateView, CategoriasListView, CategoriaUpdateView, CategoriaDeleteView,
                    ProdutoListView, ProdutoCreateView, ProdutoUpdateView, ProdutoDeleteView, ProdutoReadView
                    )

app_name = 'produtos'

urlpatterns = [
    path('', ProdutoListView.as_view(), name='lista_produto'),
    path('novo/', ProdutoCreateView.as_view(), name='novo_produto'),
    path('editar/<int:pk>/', ProdutoUpdateView.as_view(), name='atualizar_produto'),
    path('read/<int:pk>', ProdutoReadView.as_view(), name='read_produto'),
    path('delete/<int:pk>/', ProdutoDeleteView.as_view(), name='delete_produto'),

    path('fornecedor/', FornecedorListView.as_view(), name='lista_fornecedor'),
    path('fornecedor/novo/', FornecedorCreateView.as_view(), name='novo_fornecedor'),
    path('fornecedor/editar/<int:pk>/', FornecedorUpdateView.as_view(), name='atualizar_fornecedor'),
    path('fornecedor/delete/<int:pk>/', FornecedorDeleteView.as_view(), name='delete_fornecedor'),

    path('categorias/', CategoriasListView.as_view(), name='lista_categorias'),
    path('categoria/nova/', CategoriaCreateView.as_view(), name='nova_categoria'),
    path('categoria/editar/<int:pk>/', CategoriaUpdateView.as_view(), name='atualizar_categoria'),
    path('categoria/delete/<int:pk>/', CategoriaDeleteView.as_view(), name='delete_categoria'),
]

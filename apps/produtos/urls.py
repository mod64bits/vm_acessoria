from django.urls import path
from .views import (
    FornecedorCreateView,
    FornecedorListView,
    FornecedorUpdateView,
    FornecedorDeleteView

)

app_name = 'produtos'

urlpatterns = [

    path('fornecedor/', FornecedorListView.as_view(), name='lista_fornecedor'),
    path('fornecedor/novo/', FornecedorCreateView.as_view(), name='novo_fornecedor'),
    path('fornecedor/editar/<int:pk>/', FornecedorUpdateView.as_view(), name='atualizar_fornecedor'),
    path('fornecedor/delete/<int:pk>/', FornecedorDeleteView.as_view(), name='delete_fornecedor'),
]

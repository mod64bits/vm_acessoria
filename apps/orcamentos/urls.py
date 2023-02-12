from django.urls import path
from .views import (OrcamentosView, NovoOrcamento, OrcamentoUpdate, AdcionarProdutoView, AdiconarMaoDeObraView, EditarItemProdutoView, ItemProdutoDeleteView,
                    GerarOrcamentoView, ImprimirOrcamento)

app_name = 'orcamento'

urlpatterns = [

    path('novo/', NovoOrcamento.as_view(), name='novo_orcamentos'),
    path('gerar-orcamento/<int:pk>/', GerarOrcamentoView.as_view(), name='gerar_orcamento'),
    path('imprimir-orcamento/<int:pk>/', ImprimirOrcamento.as_view(), name='imprimir_orcamento'),
    path('<int:pk>/', OrcamentoUpdate.as_view(), name='update_orcamento'),
    path('adcionar/mao-de-obra/<int:pk>/', AdiconarMaoDeObraView.as_view(), name='adcionar_mao_de_obra_orcamento'),


    path('adcionar/produto/<int:pk>/', AdcionarProdutoView.as_view(), name='adcionar_produto_orcamento'),
    path('editar/produto/<int:pk>/', EditarItemProdutoView.as_view(), name='editar_produto_orcamento'),
    path('deletar/produto/<int:pk>/', ItemProdutoDeleteView.as_view(), name='deletar_produto_orcamento'),


    path('', OrcamentosView.as_view(), name='orcamentos'),
]

from django.urls import path, re_path
from .views import OrcamentosView, NovoOrcamento, OrcamentoUpdate, AdcionarProdutoView, AdiconarMaoDeObraView

app_name = 'orcamento'

urlpatterns = [

    path('novo/', NovoOrcamento.as_view(), name='novo_orcamentos'),
    path('<int:pk>/', OrcamentoUpdate.as_view(), name='update_orcamento'),
    path('adcionar/mao-de-obra/<int:pk>/', AdiconarMaoDeObraView.as_view(), name='adcionar_mao_de_obra_orcamento'),
    path('adcionar/produto/<int:pk>/', AdcionarProdutoView.as_view(), name='adcionar_produto_orcamento'),
    path('', OrcamentosView.as_view(), name='orcamentos'),
]
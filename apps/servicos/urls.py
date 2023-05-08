from django.urls import path
from .views import (
    CategoriaServicoListView,
    CategoriaServicoCreateView,
    CategoriaServicoUpdateView,
    CategoriaServicoDeleteView,
    ServicoListView,
    ServicoCreateView,
    ServicoUpdateView,
    ServicoDeleteView,


)

app_name = 'servicos'

urlpatterns = [

    path('', ServicoListView.as_view(), name='lista_servicos'),
    path('novo/', ServicoCreateView.as_view(), name='novo_servico'),
    path('atualizar/<int:pk>/', ServicoUpdateView.as_view(), name='atualizar_servico'),
    path('deletar/<int:pk>/', ServicoDeleteView.as_view(), name='deletar_servico'),

    path('categoria/', CategoriaServicoListView.as_view(), name='lista_categoria_servico'),
    path('categoria/nova/', CategoriaServicoCreateView.as_view(), name='nova_categoria_servico'),
    path('categoria/atualizar/<int:pk>/', CategoriaServicoUpdateView.as_view(), name='atualizar_categoria_servico'),
    path('deletar/categoria/<int:pk>/', CategoriaServicoDeleteView.as_view(), name='deletar_categoria_servico'),

]

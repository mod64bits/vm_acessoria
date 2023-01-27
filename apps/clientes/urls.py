from django.urls import path
from .views import (
    ClienteCreateView,
    ClienteListView,
    ClienteUpdateView,
    clientes,
    ClienteDeleteView,
    ClienteReadView
)

app_name = 'clientes'

urlpatterns = [

    path('', ClienteListView.as_view(), name='lista_clientes'),
    path('novo/', ClienteCreateView.as_view(), name='novo_cliente'),
    path('editar/<int:pk>/', ClienteUpdateView.as_view(), name='atualizar_cliente'),
    path('read/<int:pk>', ClienteReadView.as_view(), name='read_cliente'),
    path('delete/<int:pk>/', ClienteDeleteView.as_view(), name='delete_cliente'),
    path('clientes/', clientes, name='clientes'),

]

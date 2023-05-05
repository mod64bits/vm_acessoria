from django.urls import path
from .views import (
    MaoDeObraListView,
    MaoDeObraCreateView,
    TipoTipoDeMaoDeObraListView

)

app_name = 'maodeobra'

urlpatterns = [

    path('mao-de-obra/', MaoDeObraListView.as_view(), name='lista_mao_obra'),
    path('mao-de-obra/novo/', MaoDeObraCreateView.as_view(), name='nova_mao_de_obra'),
    path('tipo/', TipoTipoDeMaoDeObraListView.as_view(), name='lista_tipo_mao_de_obra'),

]

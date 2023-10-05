from django.urls import path
from .views import (PropostaView, NovaPropostaView, ListaDePropostas, NovaPropostaFormView, ProstaDetalhe,
                    GerarPdfProposta)

app_name = 'proposta'

urlpatterns = [

    path('', ListaDePropostas.as_view(), name='proposta_lista'),
    #path('<int:proposta_id>/', PropostaView.as_view(), name='proposta_detalhe'),
    path('nova/', NovaPropostaFormView.as_view(), name='nova_proposta'),
    path('buscar/<str:orcamento_id>/', NovaPropostaView.as_view(), name='proposta_redirect'),
    path('<int:pk>/', ProstaDetalhe.as_view(), name='proposta_detalhe'),
    path('pdf/<int:id>/', GerarPdfProposta.as_view(), name='proposta_pdf'),

]

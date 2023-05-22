from django.urls import path
from .views import PropostaView, NovaPropostaView

app_name = 'proposta'

urlpatterns = [

    path('<int:proposta_id>/', PropostaView.as_view(), name='proposta_detalhe'),
    path('nova/<int:orcamento>/', NovaPropostaView.as_view(), name='nova_proposta'),

]

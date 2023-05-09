from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView
from apps.core.geradorKeys import GeradorKeys
from .models import Proposta
from apps.orcamentos.models import Orcamento


class PropostaView(TemplateView):
    template_name = 'propostas/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context["now"] = timezone.now()
        return context


class NovaPropostaView(RedirectView):
    permanent = False
    query_string = True
    pattern_name = "proposta_detalhe"

    def get_redirect_url(self, *args, **kwargs):
        if Proposta.objects.get(orcamento_id=self.kwargs['orcamento_id']):
            proposta = Proposta.objects.get(orcamento_id=self.kwargs['orcamento_id'])
            return super().get_redirect_url(proposta_id=proposta.id, *args, **kwargs)

        orcamento = Orcamento.objects.get(pk=self.kwargs['orcamento_id'])
        codigo = GeradorKeys.key_proposta()
        nova_proposta = Proposta.objects.create(
            codigo=codigo,
            orcamento=orcamento,
            desconto=0,
            validade=orcamento.validade,
        )
        return super().get_redirect_url(proposta_id=nova_proposta.id, *args, **kwargs)

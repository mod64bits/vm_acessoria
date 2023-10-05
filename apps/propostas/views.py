from django.http import HttpResponse
from django.views.generic.edit import UpdateView
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView
from apps.core.geradorKeys import GeradorKeys
from .models import Proposta
from apps.orcamentos.models import Orcamento
from django.views.generic.list import ListView
from .forms import PropostaForm, SelectPropostaForm, PropostaDetalheForm
from django.views.generic import View
from pypix import Pix
from django.core.files.base import ContentFile
from django.shortcuts import render, redirect
import base64

class ListaDePropostas(ListView):
    model = Proposta
    template_name = 'propostas/lista_propostas.html'


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
        try:
            orcamento_id = int(kwargs['orcamento_id'])
            proposta = Proposta.objects.get(orcamento_id=orcamento_id)
            return proposta.get_absolute_url()
        except Proposta.DoesNotExist:
            print()
            orcamento = Orcamento.objects.get(pk=int(kwargs['orcamento_id']))
            codigo = GeradorKeys().key_proposta(orcamento.id)
            nova_proposta = Proposta.objects.create(
                codigo=codigo,
                orcamento=orcamento,
                total=orcamento.total,
                validade=orcamento.validade,
            )
            return nova_proposta.get_absolute_url()


class NovaPropostaFormView(View):
    def get(self, request, *args, **kwargs):
        form = SelectPropostaForm()
        return render(request, 'propostas/nova_proposta.html', {'form': form})

    def post(self, request, *args, **kwargs):
        return redirect('proposta:proposta_redirect', self.request.POST['orcamento'])


class ProstaDetalhe(UpdateView):
    model = Proposta
    form_class = PropostaDetalheForm
    template_name = 'propostas/proposta.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        instance = Proposta.objects.get(id=self.kwargs['pk'])
        context["orcamento"] = Orcamento.objects.get(proposta_orcamento=instance)
        context["proposta_id"] = instance.id
        return context



class GerarPdfProposta(View):
    template_name = 'propostas/proposta_impressao.html'

    def get(self, request, *args, **kwargs):
        proposta = Proposta.objects.get(id=kwargs['id'])
        return render(request, 'propostas/proposta_impressao.html', {'proposta': proposta})

from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import MaoDeObra, TipoDeMaoDeObra
from .forms import MaoDeObraForm, TipoDeMaoDeObraForm

from bootstrap_modal_forms.generic import (
    BSModalCreateView,
    BSModalUpdateView,
    BSModalDeleteView,
    BSModalReadView
)


class MaoDeObraListView(LoginRequiredMixin, ListView):
    model = MaoDeObra
    template_name = 'servicos/servico_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_open_mao_de_obra'] = True
        context['active_mao_de_obra'] = True
        return context


class MaoDeObraCreateView(LoginRequiredMixin, BSModalCreateView):
    template_name = 'servicos/nova_mao_de_obra.html'
    form_class = MaoDeObraForm
    success_message = 'Success: Mao de Obra Criado.'
    success_url = reverse_lazy('maodeobra:lista_mao_obra')


class MaoDeObraUpdateView(LoginRequiredMixin, BSModalUpdateView):
    model = MaoDeObra
    template_name = 'servicos/atualizar_mao_de_obra.html'
    form_class = MaoDeObraForm
    success_message = 'Success: Mao de Obra Atualizado.'
    success_url = reverse_lazy('maodeobra:lista_mao_obra')


class MaoDeObraDeleteView(LoginRequiredMixin, BSModalDeleteView):
    model = MaoDeObra
    template_name = 'servicos/delete_mao_de_obra.html'
    success_message = 'Success: Fornecedor excluído com sucesso.'
    success_url = reverse_lazy('maodeobra:lista_mao_obra')


class TipoTipoDeMaoDeObraListView(LoginRequiredMixin, ListView):
    model = TipoDeMaoDeObra
    template_name = 'servicos/tipo_servico_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_open_cliente'] = True
        context['active_cliente'] = True
        return context

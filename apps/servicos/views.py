from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Servico, CategoriaServico
from .forms import ServicoForm, CategoriaServicoForm

from bootstrap_modal_forms.generic import (
    BSModalCreateView,
    BSModalUpdateView,
    BSModalDeleteView,
    BSModalReadView
)


class ServicoListView(LoginRequiredMixin, ListView):
    model = Servico
    template_name = 'servicos/servico_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu_servico'] = True
        context['open_menu_servico'] = True
        context['active_servico'] = True
        return context


class ServicoCreateView(LoginRequiredMixin, BSModalCreateView):
    template_name = 'servicos/novo_servico.html'
    form_class = ServicoForm
    success_message = 'Success:Servico Criado.'
    success_url = reverse_lazy('servicos:lista_servicos')


class ServicoUpdateView(LoginRequiredMixin, BSModalUpdateView):
    model = Servico
    template_name = 'servicos/atualizar_servico.html'
    form_class = ServicoForm
    success_message = 'Success: Serviço Atualizado.'
    success_url = reverse_lazy('servicos:lista_servicos')


class ServicoDeleteView(LoginRequiredMixin, BSModalDeleteView):
    model = Servico
    template_name = 'servicos/delete_servico.html'
    success_message = 'Success: Fornecedor excluído com sucesso.'
    success_url = reverse_lazy('servicos:lista_servicos')


class CategoriaServicoListView(LoginRequiredMixin, ListView):
    model = CategoriaServico
    template_name = 'servicos/categoria_servico_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu_servico'] = True
        context['open_menu_servico'] = True
        context['active_categoria_servico'] = True
        return context


class CategoriaServicoCreateView(LoginRequiredMixin, BSModalCreateView):
    template_name = 'servicos/nova_categoria_servico.html'
    form_class = CategoriaServicoForm
    success_message = 'Success: Tipo de Serviço Criado.'
    success_url = reverse_lazy('servicos:lista_categoria_servico')


class CategoriaServicoUpdateView(LoginRequiredMixin, BSModalUpdateView):
    model = CategoriaServico
    template_name = 'servicos/atualizar_categoria_servico.html'
    form_class = CategoriaServicoForm
    success_message = 'Success: Tipo Servico Atualizado.'
    success_url = reverse_lazy('servicos:lista_categoria_servico')


class CategoriaServicoDeleteView(LoginRequiredMixin, BSModalDeleteView):
    model = CategoriaServico
    template_name = 'servicos/delete_categoria_servico.html'
    success_message = 'Success: Tipo de servico excluído com sucesso.'
    success_url = reverse_lazy('servicos:lista_categoria_servico')
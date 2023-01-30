from django.urls import reverse_lazy
from .forms import ClienteForm
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.template.loader import render_to_string
from .models import Cliente
from bootstrap_modal_forms.generic import (
    BSModalCreateView,
    BSModalUpdateView,
    BSModalDeleteView,
    BSModalReadView
)


class ClienteListView(LoginRequiredMixin, ListView):
    model = Cliente
    template_name = 'clientes/cliente_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_open_cliente'] = True
        context['active_cliente'] = True
        return context


class ClienteCreateView(LoginRequiredMixin, BSModalCreateView):
    template_name = 'clientes/novo_cliente.html'
    form_class = ClienteForm
    success_message = 'Success: Book was created.'
    success_url = reverse_lazy('clientes:lista_clientes')


class ClienteUpdateView(LoginRequiredMixin, BSModalUpdateView):
    model = Cliente
    template_name = 'clientes/atualizar_cliente.html'
    form_class = ClienteForm
    success_message = 'Success: Book was updated.'
    success_url = reverse_lazy('clientes:lista_clientes')


class ClienteDeleteView(LoginRequiredMixin, BSModalDeleteView):
    model = Cliente
    template_name = 'clientes/delete_cliente.html'
    success_message = 'Success: Book was deleted.'
    success_url = reverse_lazy('clientes:lista_clientes')


class ClienteReadView(LoginRequiredMixin, BSModalReadView):
    model = Cliente
    template_name = 'clientes/read_cliente.html'


def clientes(request):
    data = dict()
    if request.method == 'GET':
        clientes = Cliente.objects.all()
        # asyncSettings.dataKey = 'table'
        data['table'] = render_to_string(
            'clientes/includes/_cliente_table.html',
            {'clientes': clientes},
            request=request
        )
        return JsonResponse(data)

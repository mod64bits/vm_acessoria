import decimal
from django.urls import reverse_lazy
from django.urls import reverse
import locale
from decimal import Decimal
from django.db.models import Sum
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from .forms import OrcamentoProdutoForm, OrcamentoMaoDeObraForm
from bootstrap_modal_forms.generic import BSModalCreateView, BSModalUpdateView, BSModalDeleteView
from .models import Orcamento, ItemProduto, ItemMaoDeObra
from .forms import OrcamentoUpdateForm

from apps.core.ultils import GeradorKeys

from .calculos_orcamentos import ValoresOrcamento

class GerarOrcamentoView(LoginRequiredMixin, DetailView):
    model = Orcamento
    template_name = 'orcamentos/orcamento.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        orcamento = self.get_object().id
        valores = ValoresOrcamento(orcamento_id=orcamento)
        context = super().get_context_data(**kwargs)
        context['total_produtos'] = valores.total_orcamento()['total_produtos']
        context['total_maos_de_obras'] = valores.total_orcamento()['total_mao_de_obra']
        context['total_orcamento'] = valores.total_orcamento()['total_orcamento']
        return context


class ImprimirOrcamento(GerarOrcamentoView):
    template_name = 'orcamentos/orcamento_impressao.html'


class OrcamentosView(LoginRequiredMixin, ListView):
    model = Orcamento
    paginate_by = 100
    template_name = 'orcamentos/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_open_orcamento'] = True
        context['active_orcamento'] = True
        return context


class NovoOrcamento(LoginRequiredMixin, CreateView):
    form_class = OrcamentoUpdateForm
    template_name = 'orcamentos/orcamento_form.html'

    def form_valid(self, form):
        key_orcamento = GeradorKeys(user_id=self.request.user.id, cliente_id=form.instance.cliente.id)
        form.instance.codigo = key_orcamento.key()
        return super(NovoOrcamento, self).form_valid(form)


class OrcamentoUpdate(LoginRequiredMixin, UpdateView):
    model = Orcamento
    form_class = OrcamentoUpdateForm
    template_name_suffix = '_update_form'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        orcamento = self.get_object().id
        valores = ValoresOrcamento(orcamento_id=orcamento)
        context['total_produtos'] = valores.total_orcamento()['total_produtos']
        context['total_maos_de_obras'] = valores.total_orcamento()['total_mao_de_obra']
        context['total_orcamento'] = valores.total_orcamento()['total_orcamento']
        context['total_lucro'] = valores.total_orcamento()['total_lucro']
        return context


class AdcionarProdutoView(LoginRequiredMixin, BSModalCreateView):
    template_name = 'orcamentos/adcionar_item.html'
    form_class = OrcamentoProdutoForm
    success_message = 'Success: Book was created.'

    def form_valid(self, form):
        orcamento = Orcamento.objects.get(id=self.kwargs['pk'])
        qt = form.instance.quantidade
        if ItemProduto.objects.filter(produto_id=form.instance.produto.id, orcamento=orcamento).exists():
            produto = ItemProduto.objects.get(produto_id=form.instance.produto.id, orcamento=orcamento)
            form.instance = produto
            form.instance.quantidade += qt
        form.instance.orcamento = orcamento

        form.instance.total = decimal.Decimal(form.instance.preco * form.instance.quantidade)

        return super(AdcionarProdutoView, self).form_valid(form)


class AdiconarMaoDeObraView(LoginRequiredMixin, BSModalCreateView):
    template_name = 'orcamentos/adcionar_mao_de_obra.html'
    form_class = OrcamentoMaoDeObraForm
    success_message = 'Mão de obra adcionado com sucesso!'

    def form_valid(self, form):
        orcamento = Orcamento.objects.get(id=self.kwargs['pk'])
        qt = form.instance.quantidade
        if ItemMaoDeObra.objects.filter(mao_de_obra_id=form.instance.mao_de_obra.id,
                                        orcamento_id=self.kwargs['pk']).exists():
            mao_obra = ItemMaoDeObra.objects.get(mao_de_obra_id=form.instance.mao_de_obra_id,
                                                 orcamento_id=self.kwargs['pk'])
            form.instance = mao_obra
            form.instance.quantidade += qt
        else:
            form.instance.orcamento = orcamento
            form.instance.id = None

            form.instance.total = decimal.Decimal(form.instance.preco * form.instance.quantidade)

        return super(AdiconarMaoDeObraView, self).form_valid(form)


class EditarItemProdutoView(BSModalUpdateView):
    model = ItemProduto
    template_name = 'orcamentos/editar_item_produto.html'
    form_class = OrcamentoProdutoForm

    def form_valid(self, form):
        form.instance.total = decimal.Decimal(form.instance.preco * form.instance.quantidade)
        return super(EditarItemProdutoView, self).form_valid(form)


class ItemProdutoDeleteView(LoginRequiredMixin, BSModalDeleteView):
    model = ItemProduto
    template_name = 'orcamentos/delete_item_produto.html'
    success_message = 'Success: Categoria excluída com sucesso.'

    def get_success_url(self):
        orcamento = self.get_object()
        return reverse('orcamento:update_orcamento', kwargs={'pk': orcamento.orcamento.id})


    # TODO Adcionar edição de item mão de obra
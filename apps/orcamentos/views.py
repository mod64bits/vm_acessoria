import decimal
import locale
from decimal import Decimal
from django.db.models import Sum
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from .forms import OrcamentoProdutoForm, OrcamentoMaoDeObraForm
from bootstrap_modal_forms.generic import BSModalCreateView
from .models import Orcamento, ItemProduto, ItemMaoDeObra
from .forms import OrcamentoUpdateForm

from apps.core.ultils import GeradorKeys


class GerarOrcamentoView(DetailView):
    model = Orcamento
    template_name = 'orcamentos/orcamento.html'

    def total_itens(self, instancia):
        context = {
            "total": 0,
            "qt": 0
        }
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
        orcamento = self.get_object().id

        if instancia.objects.filter(orcamento_id=orcamento).exists():
            total = instancia.objects.filter(orcamento_id=orcamento).aggregate(Sum('total'))
            total_convert = total['total__sum']
            qt_itens = instancia.objects.filter(orcamento_id=orcamento).aggregate(Sum('quantidade'))
            qt = int(qt_itens['quantidade__sum'])
            context["total"] = locale.currency(total_convert, grouping=True, symbol=True)
            context['qt'] = qt
            return context
        context['total'] = locale.currency(0, grouping=True, symbol=True)
        return context

    def _total_orcamento_compras(self, instancia):

        orcamento = self.get_object().id

        _total_compra = Decimal(0)

        if instancia.objects.filter(orcamento_id=orcamento).exists():
            itens = instancia.objects.filter(orcamento_id=orcamento)

            if instancia is ItemProduto:
                for item in itens:
                    _total_compra += item.produto.preco_compra * item.quantidade
                return _total_compra

            if instancia is ItemMaoDeObra:
                for item in itens:
                    _total_compra += item.mao_de_obra.preco_compra * item.quantidade
                return _total_compra

        return _total_compra

    def calculos_total_orcamento(self):
        context = {}
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
        orcamento = self.get_object().id
        _total_mao_de_obra_venda = ItemMaoDeObra.objects.filter(orcamento_id=orcamento).aggregate(Sum('total'))
        _total_equipamentos_venda = ItemProduto.objects.filter(orcamento_id=orcamento).aggregate(Sum('total'))

        if _total_equipamentos_venda['total__sum'] is not None:
            total_equipamentos_venda = _total_equipamentos_venda['total__sum']
        else:
            total_equipamentos_venda = Decimal(0)

        if _total_mao_de_obra_venda['total__sum']:
            total_mao_de_obra_venda = _total_mao_de_obra_venda['total__sum']
        else:
            total_mao_de_obra_venda = Decimal(0)

        total_equipamentos_compra = self._total_orcamento_compras(ItemProduto)
        total_mao_de_obra_compra = self._total_orcamento_compras(ItemMaoDeObra)
        total_orcamento = total_equipamentos_venda + total_mao_de_obra_venda
        total_lucro_equipamentos = total_equipamentos_venda - total_equipamentos_compra
        total_lucro_mao_de_obra = total_mao_de_obra_venda - total_mao_de_obra_compra
        total_lucro = total_lucro_equipamentos + total_lucro_mao_de_obra

        context['total_orcamento'] = locale.currency(total_orcamento, grouping=True, symbol=True)
        context['total_lucro'] = locale.currency(total_lucro, grouping=True, symbol=True)
        context['total_lucro_equipamentos'] = locale.currency(total_lucro_equipamentos, grouping=True, symbol=True)
        context['total_lucro_mao_de_obras'] = locale.currency(total_lucro_mao_de_obra, grouping=True, symbol=True)

        return context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_produtos'] = self.total_itens(ItemProduto)
        context['total_maos_de_obras'] = self.total_itens(ItemMaoDeObra)
        context['total_orcamento'] = self.calculos_total_orcamento()
        return context


class ImprimirOrcamento(GerarOrcamentoView):
    template_name = 'orcamentos/orcamento_impressao.html'


class OrcamentosView(ListView):
    model = Orcamento
    paginate_by = 100
    template_name = 'orcamentos/index.html'


class NovoOrcamento(CreateView):
    form_class = OrcamentoUpdateForm
    template_name = 'orcamentos/orcamento_form.html'

    def form_valid(self, form):
        form.instance.codigo = GeradorKeys().key()
        return super(NovoOrcamento, self).form_valid(form)


class OrcamentoUpdate(UpdateView):
    model = Orcamento
    form_class = OrcamentoUpdateForm
    template_name_suffix = '_update_form'

    def total_itens(self, instancia):
        context = {
            "total": 0,
            "qt": 0
        }
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
        orcamento = self.get_object().id

        if instancia.objects.filter(orcamento_id=orcamento).exists():
            total = instancia.objects.filter(orcamento_id=orcamento).aggregate(Sum('total'))
            total_convert = total['total__sum']
            qt_itens = instancia.objects.filter(orcamento_id=orcamento).aggregate(Sum('quantidade'))
            qt = int(qt_itens['quantidade__sum'])
            context["total"] = locale.currency(total_convert, grouping=True, symbol=True)
            context['qt'] = qt
            return context
        context['total'] = locale.currency(0, grouping=True, symbol=True)
        return context

    def _total_orcamento_compras(self, instancia):

        orcamento = self.get_object().id

        _total_compra = Decimal(0)

        if instancia.objects.filter(orcamento_id=orcamento).exists():
            itens = instancia.objects.filter(orcamento_id=orcamento)

            if instancia is ItemProduto:
                for item in itens:
                    _total_compra += item.produto.preco_compra * item.quantidade
                return _total_compra

            if instancia is ItemMaoDeObra:
                for item in itens:
                    _total_compra += item.mao_de_obra.preco_compra * item.quantidade
                return _total_compra

        return _total_compra

    def calculos_total_orcamento(self):
        context = {}
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
        orcamento = self.get_object().id
        _total_mao_de_obra_venda = ItemMaoDeObra.objects.filter(orcamento_id=orcamento).aggregate(Sum('total'))
        _total_equipamentos_venda = ItemProduto.objects.filter(orcamento_id=orcamento).aggregate(Sum('total'))

        if _total_equipamentos_venda['total__sum'] is not None:
            total_equipamentos_venda = _total_equipamentos_venda['total__sum']
        else:
            total_equipamentos_venda = Decimal(0)

        if _total_mao_de_obra_venda['total__sum']:
            total_mao_de_obra_venda = _total_mao_de_obra_venda['total__sum']
        else:
            total_mao_de_obra_venda = Decimal(0)

        total_equipamentos_compra = self._total_orcamento_compras(ItemProduto)
        total_mao_de_obra_compra = self._total_orcamento_compras(ItemMaoDeObra)
        total_orcamento = total_equipamentos_venda + total_mao_de_obra_venda
        total_lucro_equipamentos = total_equipamentos_venda - total_equipamentos_compra
        total_lucro_mao_de_obra = total_mao_de_obra_venda - total_mao_de_obra_compra
        total_lucro = total_lucro_equipamentos + total_lucro_mao_de_obra

        context['total_orcamento'] = locale.currency(total_orcamento, grouping=True, symbol=True)
        context['total_lucro'] = locale.currency(total_lucro, grouping=True, symbol=True)
        context['total_lucro_equipamentos'] = locale.currency(total_lucro_equipamentos, grouping=True, symbol=True)
        context['total_lucro_mao_de_obras'] = locale.currency(total_lucro_mao_de_obra, grouping=True, symbol=True)

        return context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_produtos'] = self.total_itens(ItemProduto)
        context['total_maos_de_obras'] = self.total_itens(ItemMaoDeObra)
        context['total_orcamento'] = self.calculos_total_orcamento()
        return context


class AdcionarProdutoView(BSModalCreateView):
    template_name = 'orcamentos/adcionar_item.html'
    form_class = OrcamentoProdutoForm
    success_message = 'Success: Book was created.'

    def form_valid(self, form):
        orcamento = Orcamento.objects.get(id=self.kwargs['pk'])
        qt = form.instance.quantidade
        if ItemProduto.objects.filter(produto_id=form.instance.produto.id, orcamento_id=self.kwargs['pk']).exists():
            produto = ItemProduto.objects.get(produto_id=form.instance.produto.id, orcamento_id=self.kwargs['pk'])
            form.instance = produto
            form.instance.quantidade += qt
        form.instance.orcamento = orcamento

        form.instance.total = decimal.Decimal(form.instance.preco * form.instance.quantidade)

        return super(AdcionarProdutoView, self).form_valid(form)


# TODO: corrigir bug do modal com selec2 não recebe o cursor para digitar

class AdiconarMaoDeObraView(BSModalCreateView):
    template_name = 'orcamentos/adcionar_mao_de_obra.html'
    form_class = OrcamentoMaoDeObraForm
    success_message = 'Mão de obra adcionado com sucesso!'

    def form_valid(self, form):
        orcamento = Orcamento.objects.get(id=self.kwargs['pk'])
        qt = form.instance.quantidade
        if ItemMaoDeObra.objects.filter(mao_de_obra_id=form.instance.mao_de_obra.id,
                                        orcamento_id=self.kwargs['pk']).exists():
            mao_obra = ItemMaoDeObra.objects.get(mao_de_obra_id=form.instance.produto.id,
                                                 orcamento_id=self.kwargs['pk'])
            form.instance = mao_obra
            form.instance.quantidade += qt
        form.instance.orcamento = orcamento

        form.instance.total = decimal.Decimal(form.instance.preco * form.instance.quantidade)

        return super(AdiconarMaoDeObraView, self).form_valid(form)

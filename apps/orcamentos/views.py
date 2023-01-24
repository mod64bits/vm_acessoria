import decimal
import locale
from django.db.models import Sum
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import OrcamentoProdutoForm, OrcamentoMaoDeObraForm
from bootstrap_modal_forms.generic import BSModalCreateView
from .models import Orcamento, ItemProduto, ItemMaoDeObra
from .forms import OrcamentoUpdateForm


class OrcamentosView(ListView):
    model = Orcamento
    paginate_by = 100
    template_name = 'orcamentos/index.html'


class NovoOrcamento(CreateView):
    form_class = OrcamentoUpdateForm
    template_name = 'orcamentos/orcamento_form.html'


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
        return context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_produtos'] = self.total_itens(ItemProduto)
        context['total_maos_de_obras'] = self.total_itens(ItemMaoDeObra)
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
        if ItemMaoDeObra.objects.filter(mao_de_obra_id=form.instance.mao_de_obra.id, orcamento_id=self.kwargs['pk']).exists():
            mao_obra = ItemMaoDeObra.objects.get(mao_de_obra_id=form.instance.produto.id, orcamento_id=self.kwargs['pk'])
            form.instance = mao_obra
            form.instance.quantidade += qt
        form.instance.orcamento = orcamento

        form.instance.total = decimal.Decimal(form.instance.preco * form.instance.quantidade)

        return super(AdiconarMaoDeObraView, self).form_valid(form)

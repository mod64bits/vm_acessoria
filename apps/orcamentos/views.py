import decimal

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import OrcamentoProdutoForm
from bootstrap_modal_forms.generic import BSModalCreateView
from .models import Orcamento, ItemProduto
from .forms import OrcamentoUpdateForm


class OrcamentosView(ListView):
    model = Orcamento
    paginate_by = 100
    template_name = 'orcamentos/index.html'


class NovoOrcamento(CreateView):
    model = Orcamento
    fields = '__all__'


class OrcamentoUpdate(UpdateView):
    model = Orcamento
    form_class = OrcamentoUpdateForm
    template_name_suffix = '_update_form'


class AdcionarProdutoView(BSModalCreateView):
    template_name = 'orcamentos/adcionar_item.html'
    form_class = OrcamentoProdutoForm
    success_message = 'Success: Book was created.'
    #success_url = reverse_lazy('orcamento:update_orcamento')



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




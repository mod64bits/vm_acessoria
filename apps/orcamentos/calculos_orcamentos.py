import locale
from decimal import Decimal
from django.db.models import Sum
from apps.orcamentos.models import Orcamento

from apps.orcamentos.models import ItemProduto, ItemMaoDeObra


class ValoresOrcamento:
    def __init__(self, orcamento_id):
        self._orcamento = Orcamento.objects.get(id=orcamento_id)

    def total_orcamento(self):
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
        context = {}

        total_orcamento = self.total_produtos()['total'] + self.total_mao_de_obra()['total']
        total_lucro = self.total_produtos()['total_lucro'] + self.total_produtos()['total_lucro']

        context['total_produtos'] = locale.currency(self.total_produtos()['total'], grouping=True, symbol=True)
        context['total_produto_lucro'] = locale.currency(self.total_produtos()['total_lucro'], grouping=True, symbol=True)
        context['total_mao_de_obra'] = locale.currency(self.total_mao_de_obra()['total'], grouping=True, symbol=True)
        context['total_lucro_mao_de_obra'] = locale.currency(self.total_produtos()['total_lucro'], grouping=True, symbol=True)
        context['total_orcamento'] = locale.currency(total_orcamento, grouping=True, symbol=True)
        context['total_lucro'] = locale.currency(total_lucro, grouping=True, symbol=True)

        return context

    def total_mao_de_obra(self):
        context = {}
        total_lucro = Decimal(0)
        maoes_de_obras = ItemMaoDeObra.objects.filter(orcamento_id=self._orcamento)
        for item in maoes_de_obras:
            if not item.execurcao_parceiro:
                total_lucro += item.preco * item.quantidade
            else:
                total_lucro += (item.preco - item.mao_de_obra) * item.quantidade
        total = maoes_de_obras.aggregate(Sum('total'))
        context['total_lucro'] = total_lucro
        context['total'] = total['total__sum']
        return context

    def total_produtos(self):
        context = {}
        total_lucro = Decimal(0)
        produtos = ItemProduto.objects.filter(orcamento_id=self._orcamento)
        for produto in produtos:
            total_lucro += (produto.preco - produto.produto.preco_compra) * produto.quantidade
        total = produtos.aggregate(Sum('total'))
        context['total_lucro'] = total_lucro
        context['total'] = total['total__sum']
        return context

    def quabtidade_produtos(self):
        return ItemProduto.objects.filter(orcamento_id=self._orcamento.id).count()

    def quantidade_mao_de_obra(self):
        return ItemProduto.objects.filter(orcamento_id=self._orcamento).count()


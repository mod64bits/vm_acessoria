from django.db import models
from django.urls import reverse
from apps.core.models import Base
from apps.servicos.models import Servico
from apps.clientes.models import Cliente
from apps.produtos.models import Produto
from apps.core.ultils import GeradorKeys
from apps.core.ultils import Datas


class Orcamento(models.Model):
    validade = models.DateField('Validade', default=Datas().vencimento())
    STATUS_CHOICES = (
        (0, 'Não Enviado'),
        (1, 'Em Analise'),
        (2, 'Aprovado'),
        (3, 'Cancelada'),
    )
    status = models.IntegerField(
        'Situação', choices=STATUS_CHOICES, default=0, blank=True
    )
    codigo = models.CharField("Codigo", max_length=20, editable=False, default=GeradorKeys().key(), unique=True)
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
        verbose_name='Cliente',
        related_name='orcamento_cliente'
    )
    descricao = models.TextField('Descrição')

    def get_absolute_url(self):
        return reverse('orcamento:update_orcamento', kwargs={'pk': self.id})

    def total_produto(self):
        aggregate_queryset = self.produto_orcamento.aggregate(
            total=models.Sum(
                models.F('preco') * models.F('quantidade'),
                output_field=models.DecimalField()
            )
        )
        return aggregate_queryset['total']

    def total_servico(self):
        aggregate_queryset = self.produto_orcamento.aggregate(
            total=models.Sum(
                models.F('preco'),
                output_field=models.DecimalField()
            )
        )
        return aggregate_queryset['total_servico']


class ItemServico(models.Model):
    orcamento = models.ForeignKey(
        Orcamento,
        on_delete=models.CASCADE,
        verbose_name='Orçamento',
        related_name='servico_orcamento'
    )
    servico = models.ForeignKey(
        Servico,
        on_delete=models.CASCADE,
        verbose_name='Serviço',
        related_name='item_servico'
    )
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=8)
    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)


class ProdutoItemManager(models.Manager):

    def add_item(self, orcamento, produto):
        if self.filter(orcamento=orcamento, produto=produto).exists():
            created = False
            orcamento_item = self.get(orcamento=orcamento, produto=produto)
            orcamento_item.quantidade = orcamento_item.quantidade + 1
            orcamento_item.save()
        else:
            created = True
            orcamento_item = ItemProduto.objects.create(
                orcamento=orcamento, produto=produto, preco=produto.preco_compra
            )
        return orcamento_item, created
class ItemProduto(models.Model):
    orcamento = models.ForeignKey(
        Orcamento,
        on_delete=models.CASCADE,
        verbose_name='Orcamento',
        related_name='produto_orcamento'
    )
    produto = models.ForeignKey(
        Produto,
        on_delete=models.CASCADE,
        verbose_name='Produto',
        related_name='item_produto',
    )
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=8)
    total = models.DecimalField('Total', decimal_places=2, max_digits=8, null=True, blank=True)
    quantidade = models.PositiveIntegerField('Quantidade', default=1)
    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    objects = ProdutoItemManager()

    class Meta:
        verbose_name = 'Item Produto'
        verbose_name_plural = 'itens Produtos'
        ordering = ['-created']

    def __str__(self):
        return f"{self.produto}  -  {self.preco}"
    def total_produto(self):
        aggregate_queryset = self.objects.aggregate(
            total=models.Sum(
                models.F(self.preco, output_field=models.DecimalField()) * models.F(self.quantidade),

            )
        )
        return aggregate_queryset['total']

    def get_absolute_url(self):
        return reverse('orcamento:update_orcamento', kwargs={'pk': self.orcamento.id})

from django.db import models
from django.urls import reverse
from apps.core.models import Base
from apps.servicos.models import MaoDeObra
from apps.clientes.models import Cliente
from apps.empresas.models import Empresa
from apps.produtos.models import Produto
from apps.core.ultils import GeradorKeys
from apps.core.ultils import Datas


class Orcamento(models.Model):
    STATUS_CHOICES = (
        (0, 'Não Enviado'),
        (1, 'Em Analise'),
        (2, 'Aprovado'),
        (3, 'Cancelada'),
    )
    validade = models.DateField('Validade', default=Datas().vencimento())
    empresa = models.ForeignKey(
        Empresa,
        on_delete=models.CASCADE,
        verbose_name='Empresa para o Orçamento',
        related_name='empresa_orcamento',
    )

    status = models.IntegerField(
        'Situação', choices=STATUS_CHOICES, default=0, blank=True
    )
    codigo = models.CharField("Codigo", max_length=20, editable=False, unique=True)
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
        verbose_name='Cliente',
        related_name='orcamento_cliente'
    )
    descricao = models.TextField('Descrição')
    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

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


class ItemMaoDeObra(models.Model):
    execurcao_parceiro = models.BooleanField('Execultado Por Parceiro', default=False)
    orcamento = models.ForeignKey(
        Orcamento,
        on_delete=models.CASCADE,
        verbose_name='Orçamento',
        related_name='mao_obra_orcamento'
    )
    mao_de_obra = models.ForeignKey(
        MaoDeObra,
        on_delete=models.CASCADE,
        verbose_name='Mão de Obra',
        related_name='item_mao_obra'
    )
    descricao = models.TextField('Descrição', null=True, blank=True)
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=8)
    total = models.DecimalField('Total', decimal_places=2, max_digits=8, null=True, blank=True)
    quantidade = models.PositiveIntegerField('Quantidade', default=1)
    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    class Meta:
        verbose_name = 'Item mão de obra'
        verbose_name_plural = 'Itens Mãos de Obras'
        ordering = ['-created']

    def __str__(self):
        return f"{self.mao_de_obra.descricao} - {self.preco}"

    def get_absolute_url(self):
        return reverse('orcamento:update_orcamento', kwargs={'pk': self.orcamento.id})


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

    class Meta:
        verbose_name = 'Item Produto'
        verbose_name_plural = 'itens Produtos'
        ordering = ['-created']

    def __str__(self):
        return f"{self.produto}  -  {self.preco}"

    def get_absolute_url(self):
        return reverse('orcamento:update_orcamento', kwargs={'pk': self.orcamento.id})




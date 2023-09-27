from django.db import models
from django.urls import reverse
from apps.core.models import Base
from apps.servicos.models import Servico
from apps.clientes.models import Cliente
from apps.empresas.models import Empresa
from apps.produtos.models import Produto
from apps.core.ultils import GeradorKeys
from apps.core.ultils import Datas
# from .managers import OrcamentoManager
from django.db.models import signals


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
    total = models.DecimalField('Total', decimal_places=2, max_digits=8, null=True, blank=True)
    total_equipamentos = models.DecimalField('Total Equipamentos', decimal_places=2, max_digits=8, null=True,
                                             blank=True)
    total_mao_de_obra = models.DecimalField('Total Mão de Obra', decimal_places=2, max_digits=8, null=True, blank=True)
    total_lucro = models.DecimalField('Total Lucro', decimal_places=2, max_digits=8, null=True, blank=True)
    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    def __str__(self):
        return self.cliente.nome

    def get_absolute_url(self):
        return reverse('orcamento:update_orcamento', kwargs={'pk': self.id})


class ItemMaoDeObra(models.Model):
    orcamento = models.ForeignKey(
        Orcamento,
        on_delete=models.CASCADE,
        verbose_name='Orçamento',
        related_name='mao_obra_orcamento'
    )
    mao_de_obra = models.ForeignKey(
        Servico,
        on_delete=models.CASCADE,
        verbose_name='Serviço',
        related_name='item_servico'
    )
    descricao = models.TextField('Descrição', null=True, blank=True)
    valor = models.DecimalField('Preço', decimal_places=2, max_digits=8)
    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    class Meta:
        verbose_name = 'Item Mão de Obra'
        verbose_name_plural = 'Itens Maões de Obras'
        ordering = ['-created']

    def __str__(self):
        return f"{self.mao_de_obra.descricao} - {self.valor}"

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
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=8, null=True, blank=True)
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


def update_total_orcamento(sender, instance, signal, *args, **kwargs):
    orcamento = instance.orcamento
    obj = ItemProduto.objects.filter(orcamento=orcamento).values('preco')
    obj_mao_de_obra = ItemMaoDeObra.objects.filter(orcamento=orcamento).values('valor')
    total_produtos = sum(sum(produto.values()) for produto in obj)
    total_mao_de_obra = sum(sum(item.values()) for item in obj_mao_de_obra)

    _obj_produto_compra = ItemProduto.objects.filter(orcamento=orcamento)
    _obj_compra_mao_de_obra = ItemMaoDeObra.objects.filter(orcamento=orcamento)
    tota_item_compra = 0
    total_item_mao_de_obra = 0
    for item_comp in _obj_produto_compra:
        tota_item_compra += item_comp.produto.preco_compra

    for item_mao_de_obra in _obj_compra_mao_de_obra:
        total_item_mao_de_obra += item_mao_de_obra.valor

    orcamento.total_equipamentos = total_produtos
    orcamento.total_mao_de_obra = total_mao_de_obra
    orcamento.total = total_produtos + total_mao_de_obra

    orcamento.total_lucro = ((total_produtos + total_mao_de_obra) - tota_item_compra) - total_item_mao_de_obra

    orcamento.save()


signals.post_save.connect(update_total_orcamento, sender=ItemProduto)
signals.post_delete.connect(update_total_orcamento, sender=ItemProduto)

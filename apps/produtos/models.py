from django.db import models
from apps.core.models import Base


class Fornecedor(Base):
    class Meta:
        verbose_name = 'Fornecedo'
        verbose_name_plural = 'Fornecedores'
        ordering = ['nome']


class Categoria(Base):
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['nome']


class Produto(Base):
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        verbose_name='Categoria',
        related_name='p_categoria'
    )
    fornecedor = models.ForeignKey(
        Fornecedor,
        on_delete=models.CASCADE,
        verbose_name='Fornecedor',
        related_name='p_fornecedor'
    )
    preco_compra = models.DecimalField('Preço de Compra', decimal_places=2, max_digits=8)

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['nome']


from apps.core.models import Base
from django.db import models
from apps.orcamentos.models import Orcamento


class Desconto(Base):
    descricao = models.CharField('Descrição', max_length=200)
    porcetagem_desconto = models.DecimalField('Por', decimal_places=2, max_digits=8)

    class Meta:
        verbose_name = 'Desconto'
        verbose_name_plural = 'Descontos'
        ordering = ['-created']

    def __str__(self):
        return self.descricao


class Proposta(Base):
    codigo = models.CharField('Proposta Numero', max_length=30, unique=True)
    orcamento = models.ForeignKey(
        Orcamento,
        on_delete=models.CASCADE,
        verbose_name='Proposta',
        related_name='proposta_orcamento'
    )
    desconto = models.DecimalField('Por', decimal_places=2, max_digits=8, null=True, blank=True, editable=False)
    validade = models.DateField('Validade', null=True, blank=True)

    class Meta:
        verbose_name = 'Proposta'
        verbose_name_plural = 'Propostas'
        ordering = ['-created']

    def __str__(self):
        return self.codigo

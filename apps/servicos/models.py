from django.db import models
from apps.core.models import Base


class TipoDeMaoDeObra(Base):
    nome = models.CharField("Nome", max_length=100)
    verbose_name = 'Tipo Mão de Obra'
    verbose_name_plural = 'Tipos Mãos de Obras'
    ordering = ['-created']

    class Meta:
        verbose_name = 'Tipo de Mão de Obra'
        verbose_name_plural = 'Tipos de Mãoes de Obras'
        ordering = ['-created']

    def __str__(self):
        return self.nome


class MaoDeObra(models.Model):
    tipo_de_mao_de_obra = models.ForeignKey(
        TipoDeMaoDeObra, on_delete=models.CASCADE,
        verbose_name='Tipo de mão de obra',
        related_name='tipo_mao_obra'
    )
    descricao = models.TextField('Descrição')
    preco_compra = models.DecimalField('Preço Mão de Obra', decimal_places=2, max_digits=8, default=0)
    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    class Meta:
        verbose_name = 'Mão de obra'
        verbose_name_plural = 'Mãos de Obras'
        ordering = ['-created']

    def __str__(self):
        return self.descricao


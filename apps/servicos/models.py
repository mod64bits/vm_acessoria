from django.db import models
from apps.core.models import Base


class CategoriaServico(Base):
    nome = models.CharField("Nome", max_length=100, unique=True)

    class Meta:
        verbose_name = 'Categoria Serviço'
        verbose_name_plural = 'Categorias Serviços'
        ordering = ['-created']

    def __str__(self):
        return self.nome


class Servico(models.Model):
    categoria_servico = models.ForeignKey(
        CategoriaServico, on_delete=models.CASCADE,
        verbose_name='Serviço',
        related_name='categoria_servico'
    )
    descricao = models.TextField('Descrição')
    preco_compra = models.DecimalField('Valor', decimal_places=2, max_digits=8, default=0)
    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    class Meta:
        verbose_name = 'Serviços'
        verbose_name_plural = 'Serviços'
        ordering = ['-created']

    def __str__(self):
        return self.descricao


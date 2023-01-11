from django.db import models
from apps.core.models import Base


class TipoDeServico(Base):
    verbose_name = 'Tipo de Serviço'
    verbose_name_plural = 'Tipo de Serviços'
    ordering = ['-created']


class Servico(models.Model):
    tipo_servico = models.ForeignKey(TipoDeServico, on_delete=models.CASCADE)
    descricao = models.TextField('Descrição')
    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'
        ordering = ['-created']

    def __str__(self):
        return self.descricao


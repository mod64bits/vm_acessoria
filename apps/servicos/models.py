from django.db import models
from apps.core.models import Base


class TipoDeServico(Base):
    pass


class Servico(models.Model):
    tipo_servico = models.ForeignKey(TipoDeServico, on_delete=models.CASCADE)
    descricao = models.TextField('Descrição')
    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)


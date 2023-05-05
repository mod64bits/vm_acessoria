from django.db import models
from apps.core.models import Base


class Cliente(Base):
    documento = models.CharField('CPF/CNPJ', max_length=50, unique=True, null=True, blank=True)
    telefone = models.CharField('Telefone', max_length=20, unique=True, null=True, blank=True)
    email = models.EmailField('E-mail', null=True, blank=True)
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['-created']


class TelefoneContato(models.Model):
    numero = models.CharField('Telefone', max_length=20, unique=True)
    whatsApp = models.BooleanField('WhatsApp?', default=True)
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
        related_name='c_telefone',
        verbose_name='Cliente'
    )
    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    def __str__(self):
        return f"Telefone:{self.numero}, Cliente:{self.cliente.nome}"

    class Meta:
        verbose_name = 'Telefone'
        verbose_name_plural = 'Telefones'
        ordering = ['-created']



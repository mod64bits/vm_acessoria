from apps.core.models import Base
from django.db import models
from apps.orcamentos.models import Orcamento
from django.urls import reverse
from apps.core.gerador_pix import gerador_proposta_pix
from django.db.models import signals


class Proposta(models.Model):
    codigo = models.CharField('Codigo', max_length=30, unique=True)
    finalizado = models.BooleanField('Finalizado', default=False)
    orcamento = models.OneToOneField(
        Orcamento,
        on_delete=models.CASCADE,
        verbose_name='Orcamento',
        related_name='proposta_orcamento'
    )
    desconto_real = models.DecimalField('Desconto', decimal_places=2, max_digits=8, default=0, null=True, blank=True)
    desconto_porcentagem = models.DecimalField('Porcentagem', decimal_places=2, max_digits=8, null=True, blank=True, editable=False)
    total = models.DecimalField('Total', decimal_places=2, max_digits=8, null=True, blank=True)
    valor_entrada = models.DecimalField('Valor da Entrada', decimal_places=2, max_digits=8, null=True, blank=True)
    qr_code = models.ImageField('QRcode', upload_to='qrcode/%Y/%m/%d', null=True, blank=True)
    validade = models.DateField('Validade', null=True, blank=True)
    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    class Meta:
        verbose_name = 'Proposta'
        verbose_name_plural = 'Propostas'
        ordering = ['-created']

    def __str__(self):
        return self.codigo

    def get_absolute_url(self):
        return reverse('proposta:proposta_detalhe', kwargs={'pk': self.id})


def proposta_pix(sender, instance, signal, *args, **kwargs):
    proposta = instance
    if proposta.valor_entrada:
        instance.qr_code = gerador_proposta_pix(instance.codigo, instance.valor_entrada)




signals.pre_save.connect(proposta_pix, sender=Proposta)
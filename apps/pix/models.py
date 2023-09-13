from django.db import models
from apps.orcamentos.models import Orcamento


class QrPix(models.Model):
    orcamento = models.OneToOneField(Orcamento, on_delete=models.CASCADE, verbose_name='Orçamento', related_name='qr_pix')
    total = models.DecimalField('Total', decimal_places=2, max_digits=8, null=True,blank=True)
    qr_code = models.ImageField(
        'QRcode', upload_to='qrcode/%Y/%m/%d', null=True, blank=True,)

import base64
from django.core.files.base import ContentFile
from pypix import Pix
from apps.pix.models import QrPix


def novo_qrpix_orcamento(instance, value):
    qr = QrPix.objects.filter(orcamento_id=instance.id) or None
    if qr:
        if qr and qr.total == instance.total:
            return qr
        qr.objects.delete()

    _valor = value.split(' ')[1]
    valor = float(_valor.replace('.', '').replace(',', '.'))
    qr_data = generator_qrcode(valor)
    format, imgstr = qr_data.split(';base64,')
    ext = format.split('/')[-1]
    data = ContentFile(base64.b64decode(imgstr), name=f'pix_cliente{instance.id}.' + ext)
    new_qr = QrPix.objects.create(
        orcamento=instance,
        total=valor,
        qr_code=data
    )
    return new_qr



def generator_qrcode(amount):
    pix = Pix()
    pix.set_name_receiver('Marcio Oliveira de Deus')
    pix.set_city_receiver('aguasdelindoia')
    pix.set_key('04855527440')
    pix.set_identification('123')
    pix.set_zipcode_receiver('13940000')
    pix.set_description('mod64bits')
    pix.set_amount(amount)
    base64qr = pix.save_qrcode('./qrcode.png', color="green", box_size=7,
                               border=1,
                               )
    return base64qr
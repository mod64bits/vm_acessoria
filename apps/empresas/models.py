from django.db import models


class Empresa(models.Model):
    nome = models.CharField('Nome', max_length=150)
    cnpj = models.CharField('CNPJ', max_length=30, null=True, blank=True)
    logo = models.ImageField('Logo', null=True, blank=True, upload_to='logos/')

    def __str__(self):
        return self.nome

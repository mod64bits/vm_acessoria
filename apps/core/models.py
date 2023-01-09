from django.db import models


class Base(models.Model):
    nome = models.CharField('Nome', max_length=50)
    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    def __str__(self):
        return self.nome

    class Meta:
        abstract = True

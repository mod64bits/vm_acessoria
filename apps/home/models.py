from django.db import models
from django_jsonform.models.fields import JSONField


class InforcacoesGerais(models.Model):
    empresa = models.CharField('Nome da Empresa', max_length=100)
    cnpj = models.CharField('cnpj', max_length=30, null=True, blank=True)
    telefone = models.CharField('Telefone', max_length=30)
    email = models.EmailField('E-mail')
    endereco = models.TextField('Endereço', null=True, blank=True)
    facebook = models.URLField('Facebook', null=True, blank=True)
    instagram = models.URLField('Instagram', null=True, blank=True)
    twitter = models.URLField('Twitter', null=True, blank=True)

    def __str__(self):
        return self.empresa


class Contato(models.Model):
    nome = models.CharField('Nome', max_length=50)
    email = models.EmailField('E-mail')
    assunto = models.CharField('Assunto', max_length=100)
    menssagem = models.TextField('Mensagem')

    def __str__(self):
        return self.nome


class Sobre(models.Model):
    ITEMS_SCHEMA = {
        'type': 'array',  # a list which will contain the items
        'items': {
            'type': 'string'  # items in the array are strings
        }
    }

    titulo = models.CharField('Titulo', max_length=250)
    frase_destaque = models.CharField('Frase de Destaque', max_length=250, null=True, blank=True)
    descricao_curta = models.TextField('Descrição Curta', null=True, blank=True)

    destaque = JSONField(schema=ITEMS_SCHEMA, null=True, blank=True)
    imagem_destaque = models.ImageField('Imagem Sobre', upload_to='upload/home/', null=True, blank=True)
    video_destaque = models.URLField('Video Sobre', null=True, blank=True)
    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    def __str__(self):
        return self.titulo


class Marcas(models.Model):
    nome = models.CharField('Nome', max_length=20)
    logo = models.ImageField('Logo', upload_to='parceiros/logos/')


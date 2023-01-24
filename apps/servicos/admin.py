from django.contrib import admin
from .models import TipoDeMaoDeObra, MaoDeObra


class TipoMaoDeObraAdmin(admin.ModelAdmin):
    list_display = ['nome']
    search_fields = ['nome']


class MaoDeObraAdmin(admin.ModelAdmin):
    list_display = ['tipo_de_mao_de_obra', 'descricao', 'preco_mao_de_obra', 'created', 'modified']
    search_fields = ['tipo_de_mao_de_obra', 'tipo_de_mao_de_obra__nome']
    list_filter = ['created', 'modified']


admin.site.register(TipoDeMaoDeObra, TipoMaoDeObraAdmin)
admin.site.register(MaoDeObra, MaoDeObraAdmin)

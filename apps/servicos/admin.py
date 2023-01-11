from django.contrib import admin
from .models import TipoDeServico, Servico


class TipoDeServicoAdmin(admin.ModelAdmin):
    list_display = ['nome']
    search_fields = ['nome']


class ServicoAdmin(admin.ModelAdmin):
    list_display = ['tipo_servico', 'descricao', 'created', 'modified']
    search_fields = ['tipo_servico', 'tipo_servico__nome']
    list_filter = ['created', 'modified']


admin.site.register(TipoDeServico, TipoDeServicoAdmin)
admin.site.register(Servico, ServicoAdmin)

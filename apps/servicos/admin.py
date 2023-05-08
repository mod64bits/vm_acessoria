from django.contrib import admin
from .models import CategoriaServico, Servico


class CategoriaServicoAdmin(admin.ModelAdmin):
    list_display = ['nome']
    search_fields = ['nome']


class ServicoAdmin(admin.ModelAdmin):
    list_display = ['categoria_servico', 'descricao', 'preco_compra', 'created', 'modified']
    search_fields = ['categoria_servico', 'tipo_de_mao_de_obra__nome']
    list_filter = ['created', 'modified']


admin.site.register(CategoriaServico, CategoriaServicoAdmin)
admin.site.register(Servico, ServicoAdmin)

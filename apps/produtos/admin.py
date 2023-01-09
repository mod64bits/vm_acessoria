from django.contrib import admin
from .models import Fornecedor, Categoria, Produto


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'created']
    search_fields = ['created']


class FornecedorAdmin(admin.ModelAdmin):
    list_display = ['nome', 'created']
    search_fields = ['created']


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'categoria', 'fornecedor', 'categoria', 'created', 'modified']
    search_fields = ['nome', 'categoria__nome', 'fornecedor__nome']
    list_filter = ['created', 'modified']


admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Fornecedor, FornecedorAdmin)
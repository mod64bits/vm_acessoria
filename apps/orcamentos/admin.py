from django.contrib import admin

from .models import ItemProduto, Orcamento, ItemMaoDeObra


admin.site.register([ItemProduto, Orcamento, ItemMaoDeObra])

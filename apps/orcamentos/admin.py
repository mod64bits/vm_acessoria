from django.contrib import admin

from .models import ItemProduto, Orcamento


admin.site.register([ItemProduto, Orcamento])

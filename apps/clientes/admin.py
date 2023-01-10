from django.contrib import admin
from .models import Cliente, TelefoneContato


class TelefoneInline(admin.StackedInline):
    model = TelefoneContato
    extra = 1


class ClienteAdmin(admin.ModelAdmin):
    list_display = ['nome', 'documento']
    search_fields = ['-created']
    inlines = [TelefoneInline]


class TelefoneAdmin(admin.ModelAdmin):
    list_display = ['numero', 'cliente']
    search_fields = ['numero', 'cliente__nome']


admin.site.register(Cliente, ClienteAdmin)
admin.site.register(TelefoneContato, TelefoneAdmin)
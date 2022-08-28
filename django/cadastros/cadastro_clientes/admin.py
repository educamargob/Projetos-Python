from sre_constants import CATEGORY_UNI_SPACE
from django.contrib import admin
from .models import Cliente

class ListandoClientes(admin.ModelAdmin):
    list_display = ('id', 'nome_cliente', 'cnpj','data_criacao')
    list_display_links = ('id', 'nome_cliente')
    search_fields = ('nome_cliente',)
    list_filter = ('cnpj',)
    list_per_page = 15

admin.site.register(Cliente, ListandoClientes)
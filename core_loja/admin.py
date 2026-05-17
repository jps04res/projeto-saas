from django.contrib import admin
from .models import Empresa, Produto, Cliente  # Adicionado o Cliente aqui

@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ramo')
    search_fields = ('nome',)

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'empresa')
    list_filter = ('empresa',)
    search_fields = ('nome',)

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):  # Nome corrigido para ClienteAdmin
    # Aqui estão os campos que definimos no seu models.py:
    list_display = ('nome', 'cpf', 'email', 'telefone', 'cidade', 'empresa', 'ativo')
    
    # Adicionando filtros laterais para facilitar sua busca
    list_filter = ('ativo', 'cidade', 'empresa')
    
    # Adicionando uma barra de pesquisa por nome ou CPF
    search_fields = ('nome', 'cpf')
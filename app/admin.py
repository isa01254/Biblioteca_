from django.contrib import admin
from .models import Cidade, Autor, Editora, Leitor, Livro, Genero

# Definição dos Inlines (devem vir antes das classes que os utilizam)
class LivroInline(admin.TabularInline):
    model = Livro
    extra = 1 

#Configuração customizada do Autor
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    inlines = [LivroInline]

#Registro dos Modelos
# Note que o 'Autor' agora é registrado junto com sua classe de configuração 'AutorAdmin'
admin.site.register(Autor, AutorAdmin)

# Registro simples para os outros modelos
admin.site.register(Cidade)
admin.site.register(Editora)
admin.site.register(Leitor)
admin.site.register(Livro)
admin.site.register(Genero)
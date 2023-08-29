from django.contrib import admin

from .models import Autor, Categoria, Editora, Livro, Compra, ItensCompra

admin.site.register(Autor)


class AutorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email')
    search_fields = ('nome', 'email')
    list_filter = ('nome',)
    ordering = ('nome', 'email')


admin.site.register(Categoria)


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('descricao',)
    search_fields = ('descricao',)
    list_filter = ('descricao',)
    ordering = ('descricao',)
    
      
admin.site.register(Editora)


class EditoraAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    list_filter = ('nome',)
    ordering = ('nome',)


admin.site.register(Livro)


class LivroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'editora', 'categoria')
    search_fields = ('titulo', 'editora__nome', 'categoria__descricao')
    list_filter = ('editora', 'categoria')
    ordering = ('titulo', 'editora', 'categoria')
    list_per_page = 25
    
# admin.site.register(Compra)
# admin.site.register(ItensCompra)


class ItensCompraInline(admin.TabularInline):
    model = ItensCompra


@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    inlines = [ItensCompraInline]







from django.contrib import admin
from .models import Juego, Categoria


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'slug']
    prepopulated_fields = {'slug': ('nombre',)}

admin.site.register(Categoria, CategoriaAdmin)


class JuegoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'slug', 'usuario', 'plataforma', 'categoria']
    prepopulated_fields = {'slug': ('titulo',)}

admin.site.register(Juego, JuegoAdmin)

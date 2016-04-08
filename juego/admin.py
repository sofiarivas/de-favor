from django.contrib import admin
from .models import Juego


class JuegoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'slug', 'usuario', 'plataforma', 'categoria']
    prepopulated_fields = {'slug': ('titulo',)}

admin.site.register(Juego, JuegoAdmin)

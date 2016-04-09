from django import forms
from .models import Juego


class JuegoForm(forms.ModelForm):
        class Meta:
            model = Juego
            fields = ('titulo', 'plataforma', 'precio_renta', 'deposito',
                      'descripcion', 'ubicacion', 'imagen', 'prefijo', 'telefono')

from django import forms
from django.contrib.auth.decorators import login_required
from .models import Juego


class Renta(forms.Form):
    @login_required
    def post(request, Juego)
    titulo = 

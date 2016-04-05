from django.shortcuts import render
from .models import Juego
from django.views.generic import View


class Recientes(View):
    def get(self, request, fecha_alta):
        template = 'juego/reciente.html'
        juegos = Juego.objects.all()
        context = {
            'juegos': juegos
        }
        return render(request, template, context)

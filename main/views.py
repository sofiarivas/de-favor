from django.shortcuts import render
from django.views.generic import TemplateView
from juego.models import Juego
from django.core.urlresolvers import reverse



class HomeView(TemplateView):
    def get(self, request):
        template_name = "index.html"
        juegos = Juego.objects.order_by('fecha_alta').reverse()
        ctx = {'jgo': juegos}
        return render(request, template_name, ctx)


class DetalleView(TemplateView):
    def get(self, request, slug):
        juego = Juego.objects.get(slug=slug)
        template_name="detalle.html"
        contexto = {
            'juego':juego,
        }
        return render(request, template_name,contexto)

class RecientesView(TemplateView):
    def get(self, request):
        template = 'index.html'
        juegos = Juego.objects.order_by('fecha_alta').reverse()
        ctx = {'jgo': juegos}
        return render(request, template, ctx)

class PreguntasView(TemplateView):
    def get(self, request):
        template = 'faq.html'

        return render(request,template)
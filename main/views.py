from django.shortcuts import render
from django.views.generic import TemplateView
from juego.models import Juego, Categoria
from django.core.urlresolvers import reverse



class HomeView(TemplateView):
    def get(self, request):
        template_name = "index.html"
        seleccion = request.POST.get('cat')
        juegos = Juego.objects.order_by('fecha_alta').reverse()
        ctx = {'jgo': juegos,
            }
        return render(request, template_name, ctx)



class DetalleView(TemplateView):
    def get(self, request, slug):
        juego = Juego.objects.get(slug=slug)
        template_name="detalle.html"
        contexto = {
            'juego':juego,
        }
        return render(request, template_name,contexto)

class LoginView(TemplateView):
	def get(self,request):
		template_name="login.html"

		return render(request, template_name)

class PreguntasView(TemplateView):
    def get(self, request):
        template = 'faq.html'

        return render(request,template)



# class CategoriaView(TemplateView):
#     def get(self, request):
#         template_name="categoria.html"
#         juego = Juego.objects.filter('categoria')
#         contexto = {
#          'jgo':juego,
#         }
#         return render(request, template_name, contexto)

class CategoriaView(TemplateView):
    def get(self, request, nombre):
        template = 'categoria.html'
        c=Categoria.objects.get(nombre=nombre)
        print(c)
        j=Juego.objects.filter(categoria=c)
        print(j)
        ctx = {
        'c': c,
        'j': j,
        }
        return render(request, template, ctx)



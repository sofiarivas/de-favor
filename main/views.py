from django.shortcuts import render
from django.views.generic import TemplateView
from juego.models import Juego


class HomeView(TemplateView):
    def get(self, request):
        template_name = "index.html"
        return render(request, template_name)


<<<<<<< HEAD
class LoginView(TemplateView):
	def get(self,request):
		template_name="login.html"

		return render(request, template_name)
=======
class RecientesView(TemplateView):
    def get(self, request):
        template = 'index.html'
        juegos = Juego.objects.order_by('fecha_alta').reverse()
        ctx = {'jgo': juegos}
        return render(request, template, ctx)
>>>>>>> 3ce78b4dbb15f3a8e90a5612447973f682cd5356

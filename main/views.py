from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import View

# Create your views here.

class HomeView(TemplateView):
	def get(self,request):
		template_name="index.html"

		return render(request, template_name)

class DetalleView(TemplateView):
	def get(self,request):
		template_name="detalle.html"

		return render(request, template_name)


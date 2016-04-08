from django import template

register = template.Library()

from juego.models import Juego, Categoria

@register.simple_tag
def total_post():
	c=Categoria.objects.get(nombre='terror')
	j=Juego.objects.get(categoria=c)
	return j.titulo
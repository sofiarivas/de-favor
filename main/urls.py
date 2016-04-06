from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^home/$',
		views.HomeView.as_view(),
		name='home'
		),

	url(r'^detalle/(?P<slug>[-\w]+)',
		views.DetalleView.as_view(),
		name='detalle'
		),

	url(r'^preguntasfrecuentes/$',
		views.PreguntasView.as_view(),
		name='preguntasfrecuentes'
		),
 ]


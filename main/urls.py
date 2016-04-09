from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^home/$',
		views.HomeView.as_view(),
		name='home'
		),

	url(r'^todos/$',
		views.TodosView.as_view(),
		name = 'todos'
		),

	url(r'^detalle/(?P<slug>[-\w]+)',
		views.DetalleView.as_view(),
		name='detalle'
		),

	url(r'^preguntasfrecuentes/$',
		views.PreguntasView.as_view(),
		name='preguntasfrecuentes'
		),
	url(r'^login/$',
		views.LoginView.as_view(),
		name='login'
		),
	
	url(r'^categoria/(?P<nombre>[-\w]+)',
		views.CategoriaView.as_view(),
		),


]

from django.conf.urls import url
from . import views


urlpatterns=[
	url(r'^home/$', 
			views.HomeView.as_view(),
			name='home'
			),

	url(r'^detalle/$', 
			views.DetalleView.as_view(),
			name='detalle'
			),
]
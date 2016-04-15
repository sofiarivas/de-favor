from django.conf.urls import url
from . import views

urlpatterns=[
		url(r'^contacto/$', 
			views.ContactoView.as_view(),
			name='contacto'
			),
]
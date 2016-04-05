from django.conf.urls import url
from . import views



urlpatterns=[
	url(r'^home/$', 
			views.HomeView.as_view(),
			name='home'
			),


url(r'^login/$', 
			views.LoginView.as_view(),
			name='login'
			),

url(r'^contacto/$', 
			views.ContactoView.as_view(),
			name='contacto'
			),

#  ]

# urlpatterns = [
  url(r'^home/$',
      views.RecientesView.as_view(),
      name='home'),
 ]


from django.conf.urls import url
from . import views


urlpatterns = [
  url(r'^home/$',
      views.HomeView.as_view(),
      name='home'),

  url(r'^login/$',
      views.LoginView.as_view(),
      name='login'),
]

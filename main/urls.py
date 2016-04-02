from django.conf.urls import url
from . import views


urlpatterns = [
  url(r'^home/$',
      views.HomeView.as_view(),
      name='home'),
 ]

urlpatterns = [
  url(r'^home/$',
      views.RecientesView.as_view(),
      name='home'),
 ]

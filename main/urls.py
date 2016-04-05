from django.conf.urls import url
from . import views


urlpatterns = [
  url(r'^home/$',
      views.HomeView.as_view(),
      name='home'),

  url(r'^recientes/$',
      views.RecientesView.as_view(),
      name='recientes'),
 ]

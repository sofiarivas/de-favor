from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^anuncio/$',
        views.JuegoView.as_view(),
        name='anuncio'),
]

from django.conf.urls import url
from . import views
from django.contrib.auth import views as loginViews


urlpatterns = [
    url(r'^login/$',
        loginViews.login, name="login"),

    url(r'^logout/$',
        loginViews.logout, name="logout"),

    url(r'^dashboard/$', views.dashboard, name='dashboard'),

    url(r'^register/$', views.register, name='register'),
]

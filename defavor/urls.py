from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^main/',
        include('main.urls', namespace="main")),

    url(r'^cuentas/',
        include('cuentas.urls', namespace='cuentas')),

    url(r'^juego/',
        include('juego.urls', namespace='juego')),

    url('', include('social.apps.django_app.urls', namespace='social')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

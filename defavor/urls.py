from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^main/',
        include('main.urls', namespace="main")),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
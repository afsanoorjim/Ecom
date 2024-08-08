from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from Store import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.landing, name='landing')
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

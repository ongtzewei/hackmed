from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from hackmed import settings
from website import views

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('admin/', admin.site.urls),
    path('', views.get_main),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 


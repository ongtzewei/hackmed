from django.conf.urls import include, patterns, url
from django.conf.urls.static import static
from django.contrib import admin
from hackmed import settings

urlpatterns = patterns('website.views',
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^$', 'get_main', name='website-main'),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 

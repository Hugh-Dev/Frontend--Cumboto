#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'^', include('base.urls', namespace='base', app_name='base')),
    url(r'^', include('base.urls')),
    url(r'^', include('usuario.urls')),
    url(r'^', include('biblioteca.urls')),
    url(r'^', include('servicio.urls')),
    #url(r'^', include('agenda.urls')),
    url(r'^', include('django.contrib.auth.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

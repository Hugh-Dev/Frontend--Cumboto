from __future__ import unicode_literals
from django.conf.urls import url, patterns
from biblioteca.views import registrar_view
from . import views

app_name = 'biblioteca'


urlpatterns = [
	url(r'^biblioteca$', registrar_view.as_view(), name="subir"),

]

from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('show/<int:id>', views.show, name="socio_show"),
    path('estado', views.socios_estado, name="socios_estado"),
    path('comprobar', views.comprobar, name="socios_comprobar"),
]
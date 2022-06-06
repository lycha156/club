from django.urls import URLPattern, path
from .views import pagos_create, pagos_create_save

urlpatterns = [
    path('create', pagos_create_save, name="pagos_create_save"),
    path('create/<int:id>', pagos_create, name='pagos_create'),
]
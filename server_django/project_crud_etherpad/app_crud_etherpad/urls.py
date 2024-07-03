# urls.py en tu aplicación Django
from django.urls import path
from .views import create_pad

urlpatterns = [
    path('api/create_pad/', create_pad, name='create_pad'),
    # Ajusta 'api/create_pad/' según tu estructura de URL
]

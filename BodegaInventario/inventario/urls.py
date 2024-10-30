from django.urls import path

from inventario import views
from django.conf import settings
from django.conf.urls.static import static

#Rutas de la aplicacion
urlpatterns = [
    
    path('', views.inventario, name='Inventario'),
    
]

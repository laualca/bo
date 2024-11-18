from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static

#app_name = 'mantenimiento'  # Nombre de la aplicacion

#Rutas de la aplicacion
urlpatterns = [
    
    path('mantenimiento/', views.mantenimiento, name='Mantenimiento'),
    path('mantenimiento/guardar', views.guardar, name='guardar'),      # Vista para guardar un nuevo mantenimiento
    path('mantenmiento/eliminar/<int:id>/', views.eliminar, name='eliminar'),  # Vista para eliminar un mantenimiento
    path('mantenimiento/editar/<int:id>/', views.editar, name='editar'),  # Vista para editar un mantenimiento
]

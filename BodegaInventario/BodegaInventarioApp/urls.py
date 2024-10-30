from django.urls import path

from BodegaInventarioApp import views
from django.conf import settings
from django.conf.urls.static import static

#Rutas de la aplicacion
urlpatterns = [
    
    path('', views.inicio, name='Inicio'),
    path('mantenimiento/', views.mantenimiento, name='Mantenimiento'),
    path('transacciones/', views.transacciones, name='Transacciones'),
    path('reportes/', views.reportes, name='Reportes'),
    
]
#para poder visualizar las imagenes en el navegador
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
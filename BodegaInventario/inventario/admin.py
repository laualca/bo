from django.contrib import admin
from .models import Inventario

# Register your models here.
#para poder visualizarlo en la interfaz de administrador
class inventarioAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('nombre', 'marca', 'modelo', 'cantidad', 'descripcion', 'fecha', 'precio')
#Registrar el modelo inventario en el administrador de Django
admin.site.register(Inventario, inventarioAdmin)

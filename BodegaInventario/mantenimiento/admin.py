from django.contrib import admin
from .models import Mantenimiento
# Register your models here.
#Clase MantenimientoAdmin para mostrar los campos de created y updated en el administrador de Django
class MantenimientoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descripcion', 'fecha_mante', 'responsable_mante', 'created', 'updated')
    list_filter = ('fecha_mante', 'responsable_mante')
    readonly_fields = ('created', 'updated')
#Registrar el modelo Mantenimiento en el administrador de Django
admin.site.register(Mantenimiento)

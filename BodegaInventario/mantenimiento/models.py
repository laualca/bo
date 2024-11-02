from django.db import models

# Create your models here.
#Clase mantenimiento para crear la tabla en la base de datos
class Mantenimiento(models.Model):
    id_mantenimiento = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=200)
    fecha_mante = models.DateField()
    responsable_mante = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
#Clase Meta para configurar el modelo de mantenimiento en la base de datos
class Meta:
    ordering = ['fecha_mante']
    index_together = [
        ['id_mantenimiento', 'titulo']
    ]
    verbose_name = 'mantenimiento'
    verbose_name_plural = 'mantenimientos'
#Funcion para retornar el titulo del mantenimiento
    def __str__(self):
        return self.titulo
    
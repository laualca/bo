from django.db import models

# Create your models here.
#Clase inventario para crear la tabla en la base de datos
class Inventario(models.Model):
    id_codigoinv = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=80)
    marca = models.CharField(max_length=80)
    modelo = models.CharField(max_length=80)
    cantidad = models.IntegerField()
    descripcion = models.CharField(max_length=100)
    fecha = models.DateField()
    precio = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    #Clase Meta para configurar el modelo de inventario en la base de datos 
    class Meta:
        verbose_name = 'inventario'
        verbose_name_plural = 'inventarios'
        
    #Funcion para retornar el nombre del inventario
    def __str__(self):
        return self.nombre
    
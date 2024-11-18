from django.db import models

# Create your models here.

class Bienes(models.Model):
    codigo=models.CharField(primary_key=True, max_length=10)
    nombre=models.CharField(max_length=50)
    creditos=models.PositiveBigIntegerField()
    
    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nombre, self.creditos)
    

from django.db import models

# Create your models here.
class Proyect(models.Model):
  Proyecto = models.CharField(max_length=200)
  Rut = models.CharField(max_length=24, null=True)
  Nombre = models.CharField(max_length=20, null=True)
  Apellido = models.CharField(max_length=20, null=True)
  Creado_en = models.DateTimeField(auto_now_add=True)
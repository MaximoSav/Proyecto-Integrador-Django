from django.db import models

# Create your models here.

class Cliente(models.Model):
    DNI = models.AutoField(primary_key=True,)
    nombre = models.CharField(max_length=25,)
    telefono = models.BigIntegerField()
    direccion = models.CharField(max_length=40)

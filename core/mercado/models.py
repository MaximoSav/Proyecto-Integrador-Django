from django.db import models

# Create your models here.

class Cliente(models.Model):
    DNI = models.AutoField(primary_key=True,)
    nombre = models.CharField(max_length=25,)
    telefono = models.BigIntegerField()
    direccion = models.CharField(max_length=40)

class Producto (models.Model):
    id = models.AutoField(primary_key=True,)
    nombre = models.CharField(max_length=40,)
    precio = models.IntegerField()
    direccion = models.CharField(max_length=60,)
    stock = models.IntegerField()

class Categoria (models.Model):
    id = models.AutoField(primary_key=True,) 
    nombre = models.CharField(max_length = 30,)

class Divisa (models.Model):
    id = models.AutoField(primary_key=True,)
    nombre = models.CharField(max_length = 30,)
    valor = models.FloatField(null = True,)

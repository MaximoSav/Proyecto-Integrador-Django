from django.db import models

# Create your models here.


class Direccion(models.Model):
    id = models.AutoField(primary_key=True,)
    barrio = models.CharField(max_length=30)
    calle = models.CharField(max_length=30)
    numero = models.IntegerField()


class Cliente(models.Model):
    DNI = models.IntegerField(primary_key=True,)
    nombre = models.CharField(max_length=25,)
    telefono = models.BigIntegerField()
    direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE)


class Producto (models.Model):
    id = models.AutoField(primary_key=True,)
    nombre = models.CharField(max_length=40,)
    descripcion = models.CharField(max_length=255,)
    precio = models.IntegerField()
    stock = models.IntegerField()
    foto = models.ImageField(max_length=100, upload_to='fotos_productos/',
                             default='fotos_productos/default.png', blank=True,)

    def __str__(self):
        return self.nombre


class Categoria (models.Model):
    id = models.AutoField(primary_key=True,)
    nombre = models.CharField(max_length=30,)


class Divisa (models.Model):
    id = models.AutoField(primary_key=True,)
    nombre = models.CharField(max_length=30,)
    valor = models.FloatField(null=True,)


class Destacado(models.Model):
    producto = models.OneToOneField(
        Producto, on_delete=models.CASCADE, primary_key=True,)

    def __str__(self):
        return self.producto.nombre
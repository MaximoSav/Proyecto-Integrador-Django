from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.


class Direccion(models.Model):
    id = models.AutoField(primary_key=True,)
    barrio = models.CharField(max_length=30)
    calle = models.CharField(max_length=30)
    numero = models.IntegerField()


class Cliente(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True,)
    telefono = models.CharField(max_length=100)
    #direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE, default=None,)

    def __str__(self):
        return ("Cliente: {}".format(self.user.username))


class Categoria (models.Model):
    id = models.AutoField(primary_key=True,)
    nombre = models.CharField(max_length=30,)

    def __str__(self):
        return self.nombre


class Producto (models.Model):
    id = models.AutoField(primary_key=True,)
    nombre = models.CharField(max_length=40,)
    descripcion = models.CharField(max_length=255,)
    precio = models.IntegerField()
    stock = models.IntegerField()
    foto = models.ImageField(max_length=100, upload_to='fotos_productos/',
                             default='fotos_productos/default.png', blank=True,)
    categoria = models.ForeignKey(
        Categoria, on_delete=models.CASCADE, default=None,)

    def __str__(self):
        return self.nombre


class Destacado(models.Model):
    id = models.AutoField(primary_key=True,)
    imagen = models.ImageField(max_length=100, upload_to='fotos_destacados/',
                               default=None, blank=True,)

    def __str__(self):
        return str(self.id)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Cliente.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.cliente.save()

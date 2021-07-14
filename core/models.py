from django.db import models
# Create your models here.


class Login(models.Model):
    usuario = models.CharField(
        max_length=20, primary_key=True, verbose_name="Nombre Usuario")
    password = models.CharField(max_length=20, verbose_name="Contraseña")

    def __str__(self):
        return self.usuario


class Contacto(models.Model):
    nombre = models.CharField(
        max_length=30, primary_key=True, verbose_name="Nombre")
    email = models.CharField(max_length=50, verbose_name="Email")
    mensaje = models.CharField(max_length=100, verbose_name="Mensaje")

    def __str__(self):
        return self.nombre

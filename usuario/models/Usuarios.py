from django.db import models
from .Roles import Roles

class Usuarios(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.CharField(max_length=150)
    contrasena = models.CharField(max_length=250)
    nombres = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=200)
    rol = models.ForeignKey(Roles, on_delete = models.CASCADE)

    class Meta:
        db_table = "usuarios"
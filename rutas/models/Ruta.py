from django.db import models

class Ruta(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=250)
    origen = models.CharField(max_length=150)
    destino = models.CharField(max_length=150)

    class Meta:
        db_table = "ruta"

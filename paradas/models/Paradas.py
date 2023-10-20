from django.db import models
from ciudad.models.Ciudad import Ciudad

class Paradas(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=250)
    latitud = models.CharField(max_length=250)
    longitud = models.CharField(max_length=250)
    ciudad = models.ForeignKey(Ciudad, on_delete = models.CASCADE)

    class Meta:
        db_table = "paradas"

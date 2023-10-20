from django.db import models
from rutas.models.Ruta import Ruta
from paradas.models.Paradas import Paradas

class Horario(models.Model):
    id = models.AutoField(primary_key=True)
    dia_semana = models.IntegerField()
    hora_llegada = models.TimeField()
    hora_salida = models.TimeField()
    parada = models.ForeignKey(Paradas, on_delete = models.CASCADE)
    ruta = models.ForeignKey(Ruta, on_delete = models.CASCADE)

    class Meta:
        db_table = "horario"

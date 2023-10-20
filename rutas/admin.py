from django.contrib import admin
from .models.Horario import Horario
from .models.Ruta import Ruta

# Register your models here.
admin.site.register(Ruta)
admin.site.register(Horario)

from django.contrib import admin
from .models.Roles import Roles
from .models.Usuarios import Usuarios

# Register your models here.
admin.site.register(Roles)
admin.site.register(Usuarios)

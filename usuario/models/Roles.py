from django.db import models

class Roles(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=250)

    class Meta:
        db_table = "roles"

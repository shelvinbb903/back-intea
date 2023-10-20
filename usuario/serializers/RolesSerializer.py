from rest_framework import serializers
from usuario.models.Roles import Roles

class ListarRolesSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    nombre = serializers.CharField(max_length=250)
    
    class Meta:
        model = Roles
        fields = ['id', 'nombre']
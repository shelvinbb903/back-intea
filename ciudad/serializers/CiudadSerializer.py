from rest_framework import serializers
from ciudad.models.Ciudad import Ciudad

class CiudadSerializer(serializers.Serializer):
    nombre = serializers.CharField(max_length=250)
    
    def create(self, validated_data):
        ciudad = Ciudad.objects.create(**validated_data)
        
        return ciudad
    
    class Meta:
        model = Ciudad
        fields = ['id', 'nombre']

class ListarCiudadesSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    nombre = serializers.CharField(max_length=250)
    
    class Meta:
        model = Ciudad
        fields = ['id', 'nombre']

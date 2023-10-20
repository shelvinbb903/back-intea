from rest_framework import serializers
from ciudad.models.Ciudad import Ciudad
from paradas.models.Paradas import Paradas
from ciudad.serializers.CiudadSerializer import ListarCiudadesSerializer

class ParadasSerializer(serializers.Serializer):
    nombre = serializers.CharField(max_length=250)
    latitud = serializers.CharField(max_length=50)
    longitud = serializers.CharField(max_length=50)
    ciudad_id = serializers.IntegerField()
    
    """ Validar existencia de la ciudad """
    def validate_ciudad_id(self, value):
        ciudad_data = Ciudad.objects.filter(id=value)
            
        if ciudad_data.__len__() == 0:                
            raise serializers.ValidationError("Ciudad no existe")
        
        return value
    
    def create(self, validated_data):
        parada = Paradas.objects.create(**validated_data)
        
        return parada
    
    class Meta:
        model = Paradas
        fields = ['id', 'nombre', 'latitud', 'longitud']

class ListarParadasSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    nombre = serializers.CharField(max_length=250)
    latitud = serializers.CharField(max_length=50)
    longitud = serializers.CharField(max_length=50)
    ciudad = ListarCiudadesSerializer()
    
    class Meta:
        model = Paradas
        fields = ['id', 'nombre', 'latitud', 'longitud', 'ciudad']

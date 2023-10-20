from rest_framework import serializers
from rutas.models.Ruta import Ruta
from paradas.models.Paradas import Paradas
from rutas.models.Horario import Horario
from ciudad.serializers.CiudadSerializer import ListarCiudadesSerializer
from paradas.serializers.ParadasSerializer import ListarParadasSerializer
from django.db import connection
import json

class RutasSerializer(serializers.Serializer):
    nombre = serializers.CharField(max_length=250)
    origen = serializers.CharField(max_length=150)
    destino = serializers.CharField(max_length=150)
    
    def create(self, validated_data):
        ruta = Ruta.objects.create(**validated_data)
        
        return ruta
    
    class Meta:
        model = Ruta
        fields = ['id', 'nombre', 'origen', 'destino']

class ListarRutasSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    nombre = serializers.CharField(max_length=250)
    origen = serializers.CharField(max_length=150)
    destino = serializers.CharField(max_length=150)
    
    class Meta:
        model = Ruta
        fields = ['id', 'nombre', 'origen', 'destino']

class AsignarParadasSerializer(serializers.Serializer):
    dia_semana = serializers.IntegerField()
    hora_llegada = serializers.TimeField()
    hora_salida = serializers.TimeField()
    parada_id = serializers.IntegerField()
    ruta_id = serializers.IntegerField()
    
    """ Validar existencia de la parada """
    def validate_parada_id(self, value):
        parada_data = Paradas.objects.filter(id=value)
            
        if parada_data.__len__() == 0:                
            raise serializers.ValidationError("Parada no existe")
        
        return value
    
    """ Validar existencia de la ruta """
    def validate_ruta_id(self, value):
        ruta_data = Ruta.objects.filter(id=value)
            
        if ruta_data.__len__() == 0:                
            raise serializers.ValidationError("Ruta no existe")
        
        return value
    
    def create(self, validated_data):
        horario = Horario.objects.create(**validated_data)
        
        return horario
    
    class Meta:
        model = Horario
        fields = ['id', 'dia_semana', 'hora_llegada', 'hora_salida']

class ListarHorarioRutasSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    dia_semana = serializers.IntegerField()
    hora_llegada = serializers.TimeField()
    hora_salida = serializers.TimeField()
    parada = ListarParadasSerializer()
    ruta = ListarRutasSerializer()
    
    class Meta:
        model = Ruta
        fields = ['id', 'dia_semana', 'hora_llegada', 'hora_salida', 'parada', 'ruta']

class ListarParadasPorRutasSerializer(serializers.Serializer):
    
    def list_stops(self, route_id):
        list_data = Paradas.objects.raw(f'''select 
            p.*
            from horario h 
            inner join paradas p on p.id = h.id
            inner join ruta r on r.id = h.ruta_id 
            where h.ruta_id = {route_id}
            group by h.ruta_id, p.id''')
        return list_data

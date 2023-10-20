from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse
import json
from rest_framework import status
from django.http import HttpResponse
from rutas.models.Horario import Horario
from rutas.models.Ruta import Ruta
from paradas.models.Paradas import Paradas
from .serializers.RutasSerializer import RutasSerializer, ListarRutasSerializer, AsignarParadasSerializer, ListarHorarioRutasSerializer, ListarParadasPorRutasSerializer
from paradas.serializers.ParadasSerializer import ListarParadasSerializer

class RutaAPPView(APIView):
    """ 
        API rest de listar los datos de las rutas ya creadas
        
        Retorna los datos de las rutas en base de datos
        
        Rol -> Operador logístico o Pasajero
    """
    def get(self, request):
        response = dict()    
        data = dict()    
        
        queryset = Ruta.objects.all().order_by('id')
        serializer = ListarRutasSerializer(queryset, many=True)
        response["data"] = serializer.data
        return JsonResponse(status=status.HTTP_200_OK, data=response)
    
    """ 
        API rest de registrar un ruta
        
        Retorna los datos de la ruta creada o un error 
        
        Rol -> Operador logístico
    """
    def post(self, request):
        response = dict()
        
        if request.body:            
            data = json.loads(request.body)
        else:
            data = {}        
                
        serializer = RutasSerializer(data=data)
        """ Se valida si no hay errores la operacion de crear. Si hay errores, se retorna """
        if serializer.is_valid(raise_exception=False):
            ruta = serializer.create(serializer.data)
            serializer_data = ListarRutasSerializer(ruta, many=False)
            
            response["data"] = serializer_data.data
            return JsonResponse(status=status.HTTP_201_CREATED, data=response)
        else:
            response["errors"] = serializer.errors
            return JsonResponse(status=status.HTTP_400_BAD_REQUEST, data=response)
        
class DetallesRutaAPPView(APIView):
    """ 
        API rest de obtener los detalles de un ruta
        
        Retorna los datos de una ruta creada o un error 
        
        Rol -> Operador logístico o Pasajero
    """
    def get(self, request, route_id):
        response = dict()    
        data = dict()    
        
        data["ruta_id"] = route_id
        
        queryset = Horario.objects.filter(**data).order_by('id')
        serializer = ListarHorarioRutasSerializer(queryset, many=True)
        response["data"] = serializer.data
        return JsonResponse(status=status.HTTP_200_OK, data=response)
    

class AsignarRutaAPPView(APIView):
    """ 
        API rest de asignar una parada a una ruta en un horario
        
        Retorna los datos del horario establecido en la ruta o un error 
        
        Rol -> Operador logístico
    """
    def post(self, request, route_id):
        response = dict()
        
        if request.body:            
            data = json.loads(request.body)
        else:
            data = {}     
        
        data["ruta_id"] = route_id
        
        serializer = AsignarParadasSerializer(data=data)
        """ Se valida si no hay errores la operacion de crear. Si hay errores, se retorna """
        if serializer.is_valid(raise_exception=False):
            horario = serializer.create(serializer.data)
            serializer_data = ListarHorarioRutasSerializer(horario, many=False)
            
            response["data"] = serializer_data.data
            return JsonResponse(status=status.HTTP_201_CREATED, data=response)
        else:
            response["errors"] = serializer.errors
            return JsonResponse(status=status.HTTP_400_BAD_REQUEST, data=response)

class ParadasPorRutaAPPView(APIView):
    """ 
        API rest de obtener las paradas de una ruta
        
        Retorna los datos de las paradas de una ruta o un error 
        
        Rol -> Operador logístico o Pasajero
    """
    def get(self, request, route_id):
        response = dict()    
        data = dict()    
        
        serializer = ListarParadasPorRutasSerializer(data=data)
        paradas = serializer.list_stops(route_id)
        serializer = ListarParadasSerializer(paradas, many=True)
        response["data"] = serializer.data
        return JsonResponse(status=status.HTTP_200_OK, data=response)
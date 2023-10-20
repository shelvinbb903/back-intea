from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse
import json
from rest_framework import status
from django.http import HttpResponse
from .serializers.CiudadSerializer import CiudadSerializer, ListarCiudadesSerializer

class CiudadAPPView(APIView):
    """ 
        API rest de registrar una ciudad. 
        
        Retorna los datos de la ciudad registrada o un error.  
              
        Rol -> Operador logístico.
    """
    def post(self, request):
        response = dict()
        
        if request.body:            
            data = json.loads(request.body)
        else:
            data = {}        
                
        serializer = CiudadSerializer(data=data)
        """ Se valida si no hay errores la operacion de crear. Si hay errores, se retorna """
        if serializer.is_valid(raise_exception=False):
            ciudad = serializer.create(serializer.data)
            serializer_data = ListarCiudadesSerializer(ciudad, many=False)
            
            response["data"] = serializer_data.data
            return JsonResponse(status=status.HTTP_201_CREATED, data=response)
        else:
            response["errors"] = serializer.errors
            return JsonResponse(status=status.HTTP_400_BAD_REQUEST, data=response)
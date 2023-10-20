from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse
import json
from rest_framework import status
from django.http import HttpResponse
from .serializers.UsuariosSerializer import UsuariosSerializer, ListarUsuariosSerializer, LoginSerializer
import hashlib
import jwt

from rest_framework_jwt.settings import api_settings

class LoginAPPView(APIView):
    """ 
        API rest de Login.
        
        Retorna los datos de la sesion del usuario o un error si el usuario y/o contraseña son incorrectos
        
        Rol -> No Aplica
    """
    def post(self, request):
        response = dict()
        
        if request.body:            
            data = json.loads(request.body)
        else:
            data = {}  
        
        serializer = LoginSerializer(data=data)
        """ Se valida si no hay errores la operacion de crear. Si hay errores, se retorna """
        if serializer.is_valid(raise_exception=False):
            data["contrasena"] = hashlib.md5(data["contrasena"].encode()).hexdigest()
            user = serializer.login(data["usuario"], data["contrasena"])
            serializer_data = ListarUsuariosSerializer(user, many=False)
                                  
            encoded_jwt = jwt.encode(serializer_data.data, 'secret', algorithm='HS256')
            response["token"] = encoded_jwt.decode()
            response["data"] = serializer_data.data
                        
            return JsonResponse(status=status.HTTP_200_OK, data=response)
        else:
            response["errors"] = serializer.errors
            return JsonResponse(status=status.HTTP_400_BAD_REQUEST, data=response) 

class RegisterAPPView(APIView):
    """ 
        API rest de registro del usuario.
        
        Retorna los datos del usuario creado o un error 
        
        Rol -> No Aplica
    """
    def post(self, request):
        response = dict()
        
        if request.body:            
            data = json.loads(request.body)
        else:
            data = {}
        
        data["contrasena"] = hashlib.md5(data["contrasena"].encode()).hexdigest()
        
        serializer = UsuariosSerializer(data=data)
        """ Se valida si no hay errores la operacion de crear. Si hay errores, se retorna """
        if serializer.is_valid(raise_exception=False):
            
            usuario = serializer.create(serializer.data)
            serializer_data = ListarUsuariosSerializer(usuario, many=False)
            
            response["data"] = serializer_data.data
            return JsonResponse(status=status.HTTP_201_CREATED, data=response)
        else:
            response["errors"] = serializer.errors
            return JsonResponse(status=status.HTTP_400_BAD_REQUEST, data=response)  
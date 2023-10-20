from usuario.models.Usuarios import Usuarios
from usuario.models.Roles import Roles
from rest_framework import serializers
from .RolesSerializer import ListarRolesSerializer

class UsuariosSerializer(serializers.Serializer):
    usuario = serializers.CharField(max_length=150)
    contrasena = serializers.CharField(max_length=250)
    nombres = serializers.CharField(max_length=200)
    apellidos = serializers.CharField(max_length=200)
    rol_id = serializers.IntegerField()
    
    """ Validar existencia del usuario """
    def validate_usuario(self, value):
        usuario_data = Usuarios.objects.filter(usuario=value)
            
        if usuario_data.__len__() > 0:                
            raise serializers.ValidationError("Usuaio ya existe")
        
        return value
    
    """ Validar existencia del rol """
    def validate_rol_id(self, value):
        rol_data = Roles.objects.filter(id=value)
            
        if rol_data.__len__() == 0:                
            raise serializers.ValidationError("Rol no existe")
        
        return value
    
    def create(self, validated_data):
        usuario = Usuarios.objects.create(**validated_data)
        
        return usuario
    
    class Meta:
        model = Usuarios
        fields = ['id', 'usuario', 'contrasena', 'nombres', 'apellidos']

class LoginSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    usuario = serializers.CharField(max_length=150)
    contrasena = serializers.CharField(max_length=250)
    nombres = serializers.CharField(max_length=200, required=False)
    apellidos = serializers.CharField(max_length=200, required=False)
    
    def login(self, usuario, contrasena):
        usuario_data = Usuarios.objects.filter(usuario=usuario, contrasena=contrasena)
        
        if usuario_data.__len__() == 0:                
            raise serializers.ValidationError("Usuario no existe")
        
        return usuario_data.first()

class ListarUsuariosSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    usuario = serializers.CharField(max_length=150)
    contrasena = serializers.CharField(max_length=250)
    nombres = serializers.CharField(max_length=200)
    apellidos = serializers.CharField(max_length=200)
    rol = ListarRolesSerializer()
    
    class Meta:
        model = Usuarios
        fields = ['id', 'usuario', 'contrasena', 'nombres', 'apellidos', 'rol']
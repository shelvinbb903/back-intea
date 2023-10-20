import jwt
from django.http import HttpResponseForbidden
 
WHITELISTED_URLS = [
    "/api/users/login",
    "/api/users/register",
    "/docs/",
    "/redocs/"
]

def validate_rol(get_response):

    def middleware(request):
        if request.path not in WHITELISTED_URLS:            
            
            # Validar si se envia el token
            if 'token' not in request.headers:
                return HttpResponseForbidden("El token debe ser enviado en el servicio")
                                
            token = request.headers['token']            
            decoded_data = jwt.decode(jwt=token, key='secret', algorithms=["HS256"])
            
            if request.method == 'POST' and decoded_data["rol"]["id"] != 1:
                return HttpResponseForbidden("El usuario debe ser un Operador logístico")
            else:
                if request.method == 'GET' and (decoded_data["rol"]["id"] != 1 and decoded_data["rol"]["id"] != 2):
                    return HttpResponseForbidden("El usuario debe ser un Operador logístico o un Pasajero")
            
            
        response = get_response(request)
        return response

    return middleware
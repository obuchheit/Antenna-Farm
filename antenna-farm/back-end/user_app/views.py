from django.contrib.auth import authenticate
from .models import AppUser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_404_NOT_FOUND, HTTP_400_BAD_REQUEST, HTTP_204_NO_CONTENT
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class Sign_up(APIView):
    def post(self, request):
        user = AppUser.objects.create_user(**request.data)
        token = Token.objects.create(user=user)

        return Response(
            {"user": user.username, 'email': user.email, "token": token.key}, status=HTTP_201_CREATED
        )
    
class Log_in(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get("password")

        user = authenticate(username=username, password=password)

        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key, "user": user.username})
        
        else:
            return Response(
                "Username or Password were incorrect", status=HTTP_404_NOT_FOUND
            )
        
class Info(APIView):
    pass
from django.contrib.auth import authenticate, login, logout
from .models import AppUser
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_404_NOT_FOUND, HTTP_400_BAD_REQUEST, HTTP_204_NO_CONTENT
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class SignUp(APIView):
    def post(self, request):
        data = request.data
        email = data.get('email')
        username = data.get('username')

        #Queries to see if username or email are already in use.
        if AppUser.objects.filter(Q(email=email) | Q(username=username)).exists():
                return Response({"error": "Email or username already in use"}, status=HTTP_400_BAD_REQUEST)

        user = AppUser.objects.create_user(email=email, username=username, password=request.data.get("password"))
        
        token = Token.objects.create(user=user)
        return Response({"user": user.email, "token": token.key}, status=HTTP_201_CREATED)   


        
    
class LogIn(APIView):
    def post(self, request):
        data = request.data

        identifier = data.get('identifier')
        password = data.get("password")

        user = AppUser.objects.filter(Q(email=identifier) | Q(username=identifier)).first()

        if user: 
             user = authenticate(username=user.email, password=password)
             if user:
                  token, created = Token.objects.get_or_create(user=user)
                  return Response({"token": token.key, "user": user.email})
             
        return Response({"error": "Invalid credentials"}, status=HTTP_400_BAD_REQUEST)
    
class Info(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"email": request.user.email, "username": request.user.username})


class LogOut(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=HTTP_204_NO_CONTENT)
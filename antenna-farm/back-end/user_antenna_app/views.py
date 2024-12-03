from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.exceptions import ValidationError
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT
from user_app.views import TokenReq
from .serializers import AllAntennasSerializer

from .models import SavedAntennas

class AntennaManager(TokenReq):
    def get_an_antenna(self, id):
        return get_object_or_404(SavedAntennas, id=id)
    
    def post(self, requst):
        pass

    
    def delete(self, request, id):
        antenna = self.get_an_antenna(id)
        antenna.delete()
        return Response(HTTP_204_NO_CONTENT)
    

class AllAntennas(TokenReq):
    def get(self, request):
        try: 
            all_antennas = request.user.saved_antennas.all()

            ser_all_antennas = AllAntennasSerializer(all_antennas, many=True)

            response_data = {
                'saved_antennas': ser_all_antennas
            }

            return Response(response_data, status=HTTP_200_OK)
        
        except Exception as e:
            return Response({"error": str(e)}, status=HTTP_400_BAD_REQUEST)
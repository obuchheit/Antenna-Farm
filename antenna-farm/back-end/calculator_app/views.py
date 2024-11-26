from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser

class Calculator(APIView):
    def post(self, request):
        data = request.data
        operation = data.get('operation')
        num1 = float(data.get('num1'))
        num2 = float(data.get('num2'))

        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            if num2 != 0:
                result = num1 / num2
            else:
                return Response({"error": "Cannot divide by zero"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"error": "Invalid operation"}, status=status.HTTP_400_BAD_REQUEST)

        return Response({"result": result})
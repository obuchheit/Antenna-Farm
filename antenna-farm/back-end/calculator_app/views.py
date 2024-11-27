from django.http import JsonResponse
import logging

logger = logging.getLogger(__name__)


def calculate(request):
    try:
        num1 = float(request.GET.get('num1', 0))
        num2 = float(request.GET.get('num2', 0))
        operation = request.GET.get('operation', '+').strip()
        
        if operation == '-':
            result = num1 - num2
        elif operation == 'plus':
            result = num1 + num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            result = num1 / num2 if num2 != 0 else 'Cannot divide by zero'
        else:
            result = 'Invalid operation'

        
        return JsonResponse({'result': result})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)

from django.http import JsonResponse
import math

def yagi_uda_design(request):
    freq = float(request.GET.get())
    unit = request.GET.get('unit', 'standard')
    hertz = float(request.GET.get('hertz', 1))
    diameter = float(request.GET.get('diameter', 1.6))
    freq = freq * hertz



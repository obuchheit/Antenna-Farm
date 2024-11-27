from django.http import JsonResponse

def dipole_calculate(request):
    try:
        frequncy = float(request.GET.get('freq', 0)) * int(request.GET.get('hertz', 1))
        wave_length = request.GET.get('waveLength', 'half')
        unit = request.GET.get('unit', 'Standard')
        result = 0

        if unit == "Standard":
            if wave_length == "half":
                wave_length = 468
            elif wave_length == 'quarter':
                wave_length = 234
            else:
                wave_length = 1005
        else:
            if wave_length == "half":
                wave_length = 468
            elif wave_length == 'quarter':
                wave_length = 234
            else:
                wave_length = 1005
        
   




# Create your views here.

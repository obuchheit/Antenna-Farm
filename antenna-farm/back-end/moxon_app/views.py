from django.http import JsonResponse
import math

def moxon_calculate(request):
    try:
        freq = float(request.GET.get('freq', 0))
        wave_length = request.GET.get('waveLength', 'half')
        unit = request.GET.get('unit', 'standard')
        hertz = float(request.GET.get('hertz', 1))
        diameter = 1

        freq = freq * hertz

        def feet_to_inches(len):
            whole_feet = int(len)  # Get the whole feet part
            remaining_inches = (len - whole_feet) * 12  # Get the remaining inches part after extracting feet

            whole_inches = int(remaining_inches)  # Get the whole inch part
            decimal_inches = remaining_inches - whole_inches  # Get the decimal part of inches

            # Convert the decimal part into a fraction with denominator 32
            numerator = int(round(decimal_inches * 32))
            denominator = 32

            # Simplify the fraction
            while numerator % 2 == 0 and denominator % 2 == 0:
                numerator //= 2
                denominator //= 2

            # Build the result string
            if numerator == 0:
                return f"{whole_feet}' {whole_inches}\""
            elif denominator == 1:
                return f"{whole_feet}' {whole_inches + numerator}\""
            else:
                return f"{whole_feet}' {whole_inches} {numerator}/{denominator}\""
            

        wave = 299792.5 / freq
        dw = 0.4342945 * math.log(diameter / wave)

        a = -0.0008571428571 * (dw * dw) - 0.009571428571 * dw + 0.3398571429
        b = -0.002142857143 * (dw * dw) - 0.02035714286 * dw + 0.008285714286
        c = 0.001809523381 * (dw * dw) + 0.01780952381 * dw + 0.05164285714
        d = 0.001 * dw + 0.07178571429







    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)

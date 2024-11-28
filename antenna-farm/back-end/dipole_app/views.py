from django.http import JsonResponse


def dipole_calculate(request):
    try:
        freq = float(request.GET.get('freq', 0))
        wave_length = request.GET.get('waveLength', 'half')
        unit = request.GET.get('unit', 'standard')
        hertz = float(request.GET.get('hertz', 1))

        freq = freq * hertz

        print(f"Received parameters: freq={freq}, hertz={hertz}, waveLength={wave_length}, unit={unit}")


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



        if unit == "standard":
            if wave_length == "half":
                wave_length = 468
            elif wave_length == 'quarter':
                wave_length = 234
            else:
                wave_length = 1005

            total_len = wave_length / freq

            full_len = feet_to_inches(total_len)
            el_len = feet_to_inches(total_len/2)

            
            
        elif unit == "metric":
            if wave_length == "half":
                wave_length = 143
            elif wave_length == 'quarter':
                wave_length = 121.5
            else:
                wave_length = 306

            total_len = wave_length / freq
            elem_len = total_len / 2

            full_len = f"{total_len} meters"
            el_len = f"{elem_len} meters"

        else:
            return JsonResponse('Invalid Input')



        
        return JsonResponse({'fullLength': full_len, 'elementLength': el_len})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)
        
   




# Create your views here.

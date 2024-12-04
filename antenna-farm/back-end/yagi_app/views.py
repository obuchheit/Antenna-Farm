from django.http import JsonResponse
from rest_framework.status import HTTP_201_CREATED, HTTP_404_NOT_FOUND, HTTP_400_BAD_REQUEST, HTTP_204_NO_CONTENT
import math

def dl6wu_yagi(request):
    try:
        freq = float(request.GET.get('freq', 0))
        wave_length = request.GET.get('waveLength', 'half')
        unit = request.GET.get('unit', 'standard')
        hertz = float(request.GET.get('hertz', 1))
        freq = freq * hertz

        ##material = request.GET.get('material', 'coppper')


        #Ensure useState reflects
        diameter = float(request.GET.get('diameter', 5))
        boom_diameter = float(request.GET.get('boomDiameter', 20))
        boom_relation = request.GET.get('boomRelation', 'center_connected')
        num_elements = int(request.GET.get('elements'))
        
        diameter = diameter / 1000
        boom_diameter = boom_diameter/1000



        # Constants
        c = 299792458  # Speed of light in m/s
        wavelength = c / (freq * 1e6)  # Wavelength in meters
        
        # Scaling factors from DL6WU design
        director_length_factor = 0.97775  # Fraction of wavelength for directors
        reflector_length_factor = 1.05  # Fraction of wavelength for reflector
        
        """TODO:Boom Correction needs updating as well as wavelength correlation to the element lengths."""
        # Boom correction factor
        boom_correction_factor = 1.0
        if boom_relation == "center_connected":
            boom_correction_factor = 0.98
        elif boom_relation == "isolated_above":
            boom_correction_factor = 0.97
        # "insulated_boom" leaves boom_correction_factor at 1.0
        

        # Correction for wire and boom diameters
        def length_correction(length):
            # Apply boom and wire corrections
            corrected_length = length - (diameter + boom_diameter) * 0.5
            corrected_length *= boom_correction_factor
            return corrected_length

        # Calculate element lengths
        driven_element_length = length_correction(0.5 * wavelength)  # Half-wave dipole
        reflector_length = length_correction(reflector_length_factor * driven_element_length)
        director_lengths = [
            length_correction(director_length_factor * driven_element_length * (1 - i * (0.004 * wavelength)))
            for i in range(num_elements - 2)
        ]
        
        """
        Spacing Block
        ==============================================================================================
        """

        driven_element_spacing = 0.2 * wavelength
        dir_spacing = []
        space_from_reflector = []

        spacing_factors = [0.075, 0.18, 0.215, 0.25, 0.28, 0.3, 0.315, 0.33, 0.345, 0.36, 0.375, 0.385, 0.39, 0.395]  

        total = driven_element_spacing

        for i in range(num_elements-1):
            if i < 14:
                dir_spacing.append(wavelength*spacing_factors[i])
            else:
                dir_spacing.append(wavelength*0.4)

            total += wavelength*spacing_factors[i]
            space_from_reflector.append(total)
    
                


        print(f"Reflector Length: {reflector_length}")
        #print(f"Driver Space: {driven_element_spacing}")
        print(f"Driver Length: {driven_element_length}")
        # print(f"Director Spacing: {dir_spacing}")
        # print(f"Total Spacing: {space_from_reflector}")
        print(f"Director Lengths: {director_lengths}")


        return JsonResponse({
            'reflectorLength': reflector_length, 
            'driverLength': driven_element_length,
            'driverSpace': driven_element_spacing,
            'dirSpacing': dir_spacing,
            'dirSpacingFromReflector': space_from_reflector,
            'dirLengths': director_lengths})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=HTTP_400_BAD_REQUEST)
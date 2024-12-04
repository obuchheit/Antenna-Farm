def dl6wu_yagi(frequency, num_elements, wire_diameter, boom_diameter, boom_relation):
    # Constants
    c = 299792458  # Speed of light in m/s
    wavelength = c / (frequency * 1e6)  # Wavelength in meters
    
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
        corrected_length = length - (wire_diameter + boom_diameter) * 0.5
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


# Example usage
frequency = 144.0  # Operating frequency in MHz (e.g., 144 MHz)
num_elements = 8  # Number of elements
wire_diameter = 0.005  # Element wire diameter in meters (e.g., 5 mm)
boom_diameter = 0.02  # Boom diameter in meters (e.g., 20 mm)
boom_relation = "center_connected"  # Choose: "center_connected", "isolated_above", or "insulated_boom"

yagi_dimensions = dl6wu_yagi(frequency, num_elements, wire_diameter, boom_diameter, boom_relation)


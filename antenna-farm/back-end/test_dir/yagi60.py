def dl6wu_yagi(frequency, num_elements, wire_diameter, boom_diameter, boom_relation):
    """
    Calculate the dimensions of a DL6WU Yagi antenna, including boom corrections.

    Args:
        frequency (float): Operating frequency in MHz.
        num_elements (int): Number of elements in the antenna.
        wire_diameter (float): Diameter of the element wires in meters.
        boom_diameter (float): Diameter of the boom in meters.
        boom_relation (str): Relationship between elements and the boom.
            Options:
                "center_connected" - Elements are mounted at the center of a conductive boom and electrically connected.
                "isolated_above" - Elements are isolated or mounted above the boom.
                "insulated_boom" - Elements are mounted on an insulated boom.

    Returns:
        dict: A dictionary with calculated dimensions, including element lengths, positions, and boom length.
    """
    # Constants
    c = 299792458  # Speed of light in m/s
    wavelength = c / (frequency * 1e6)  # Wavelength in meters
    
    # Scaling factors from DL6WU design
    director_length_factor = 0.985  # Fraction of wavelength for directors
    element_spacing = 0.2 * wavelength  # Spacing between elements
    #Needs to be 
    reflector_length_factor = 1.05  # Fraction of wavelength for reflector
    
    # Boom correction factor
    boom_correction_factor = 1.0
    if boom_relation == "center_connected":
        boom_correction_factor = 0.98
    elif boom_relation == "isolated_above":
        boom_correction_factor = 1.02
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
        length_correction(director_length_factor * driven_element_length * (1 - i * 0.005))
        for i in range(num_elements - 2)
    ]
    
    # Calculate element positions along the boom
    positions = [0]  # Reflector at position 0
    for i in range(1, num_elements):
        positions.append(positions[-1] + element_spacing)
    
    # Calculate the total boom length
    boom_length = positions[-1]  # Total length of the boom is the last element's position
    
    # Combine results into a dictionary
    elements = {
        "Reflector": {"length": reflector_length, "position": positions[0]},
        "Driven Element": {"length": driven_element_length, "position": positions[1]},
    }
    for i, length in enumerate(director_lengths):
        elements[f"Director {i + 1}"] = {"length": length, "position": positions[i + 2]}
    
    return {
        "elements": elements,
        "boom_length": boom_length,
        "boom_correction_factor": boom_correction_factor,
    }

# Example usage
frequency = 144.0  # Operating frequency in MHz (e.g., 144 MHz)
num_elements = 7  # Number of elements
wire_diameter = 0.005  # Element wire diameter in meters (e.g., 5 mm)
boom_diameter = 0.02  # Boom diameter in meters (e.g., 20 mm)
boom_relation = "center_connected"  # Choose: "center_connected", "isolated_above", or "insulated_boom"

yagi_dimensions = dl6wu_yagi(frequency, num_elements, wire_diameter, boom_diameter, boom_relation)

print("Boom Length:", f"{yagi_dimensions['boom_length']:.3f} m")
print("Boom Correction Factor:", yagi_dimensions['boom_correction_factor'])
for element, specs in yagi_dimensions['elements'].items():
    print(f"{element}: Length = {specs['length']:.3f} m, Position = {specs['position']:.3f} m")

def dl6wu_yagi(frequency, num_elements, wire_diameter, boom_diameter):
    """
    Calculate the dimensions of a DL6WU Yagi antenna with corrections for wire and boom diameters.
    
    Args:
        frequency (float): Operating frequency in MHz.
        num_elements (int): Number of elements in the antenna.
        wire_diameter (float): Diameter of the element wires in meters.
        boom_diameter (float): Diameter of the boom in meters.

    Returns:
        dict: A dictionary with element lengths and spacings.
    """
    # Constants
    c = 299792458  # Speed of light in m/s
    wavelength = c / (frequency * 1e6)  # Wavelength in meters
    
    # Scaling factors for the DL6WU design
    director_length_factor = 0.985  # Fraction of wavelength
    element_spacing = 0.2 * wavelength  # Approx. spacing (can vary slightly)
    reflector_length_factor = 1.05  # Fraction of wavelength
    
    # Correction factor for element lengths (wire thickness and boom diameter effects)
    length_correction = lambda length: length - (wire_diameter + boom_diameter) * 0.5
    
    # Calculate the driven element
    driven_element_length = length_correction(0.5 * wavelength)  # Half-wave dipole
    
    # Calculate reflector length
    reflector_length = length_correction(reflector_length_factor * driven_element_length)

    # Calculate directors
    director_lengths = [
        length_correction(director_length_factor * driven_element_length * (1 - i * 0.005))
        for i in range(num_elements - 2)
    ]
    
    # Calculate element positions along the boom
    positions = [0]  # Reflector at 0
    for i in range(1, num_elements):
        positions.append(positions[-1] + element_spacing)

    # Combine results into a dictionary
    elements = {
        "Reflector": {"length": reflector_length, "position": positions[0]},
        "Driven Element": {"length": driven_element_length, "position": positions[1]},
    }
    
    for i, length in enumerate(director_lengths):
        elements[f"Director {i + 1}"] = {"length": length, "position": positions[i + 2]}

    return elements

# Example usage
frequency = 144.0  # Operating frequency in MHz (e.g., 144 MHz)
num_elements = 7  # Number of elements
wire_diameter = 0.005  # Element wire diameter in meters (e.g., 5 mm)
boom_diameter = 0.02  # Boom diameter in meters (e.g., 20 mm)

yagi_dimensions = dl6wu_yagi(frequency, num_elements, wire_diameter, boom_diameter)

for element, specs in yagi_dimensions.items():
    print(f"{element}: Length = {specs['length']:.3f} m, Position = {specs['position']:.3f} m")

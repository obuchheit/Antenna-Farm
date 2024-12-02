def calculate_yagi_uda(frequency, num_directors, element_diameter):
    """
    Calculate dimensions for a Yagi-Uda antenna with decreasing director lengths.
    
    Parameters:
        frequency (float): Frequency in MHz.
        num_directors (int): Number of directors.
        element_diameter (float): Diameter of the antenna elements in meters.

    Returns:
        dict: A dictionary with dimensions of the antenna components.
    """
    # Constants
    speed_of_light = 3e8  # m/s
    wavelength = speed_of_light / (frequency * 1e6)  # Convert MHz to Hz and calculate wavelength
    
    # Element lengths as fractions of the wavelength
    reflector_length = 0.5 * wavelength * 1.05  # Reflector length ~ 105% of half-wavelength
    driven_length = 0.5 * wavelength  # Driven element length ~ 100% of half-wavelength
    
    # Spacing as fractions of the wavelength
    reflector_spacing = 0.15 * wavelength  # Reflector spacing ~ 0.15 of wavelength
    director_spacing = 0.2 * wavelength  # Typical spacing between directors
    
    # Calculate the total boom length
    boom_length = reflector_spacing + (num_directors - 1) * director_spacing
    
    # Create a list for all element positions and lengths
    elements = []
    elements.append({"type": "Reflector", "length": reflector_length, "position": 0})
    elements.append({"type": "Driven", "length": driven_length, "position": reflector_spacing})
    
    # Calculate and add directors with decreasing lengths
    for i in range(num_directors):
        # Decrease the length of each director progressively by 1-2% of the wavelength
        director_length = 0.5 * wavelength * (1 - (i + 1) * 0.01)  # Reduce length by 1% per director
        position = reflector_spacing + (i + 1) * director_spacing
        elements.append({"type": f"Director {i + 1}", "length": director_length, "position": position})
    
    return {
        "frequency": frequency,
        "wavelength": wavelength,
        "element_diameter": element_diameter,
        "boom_length": boom_length,
        "elements": elements
    }

# Example usage
antenna = calculate_yagi_uda(frequency=144, num_directors=5, element_diameter=0.01)
for element in antenna["elements"]:
    print(f"{element['type']} - Length: {element['length']:.2f} m, Position: {element['position']:.2f} m")

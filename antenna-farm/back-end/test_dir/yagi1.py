def yagi_antenna_dimensions(frequency, num_directors, boom_diameter, wire_diameter):
    """
    Calculate the dimensions of a Yagi antenna.

    Parameters:
        frequency (float): The frequency of operation in MHz.
        num_directors (int): The number of directors for the antenna.
        boom_diameter (float): The diameter of the boom in meters.
        wire_diameter (float): The diameter of the wire in meters.

    Returns:
        dict: A dictionary containing the dimensions of the antenna.
    """
    # Speed of light in m/s
    c = 299792458

    # Convert frequency to Hz
    frequency_hz = frequency * 1e6

    # Wavelength in meters
    wavelength = c / frequency_hz

    # Element lengths as a fraction of the wavelength
    driven_element_length = 0.473 * wavelength  # Typically 0.475 * wavelength
    reflector_length = 0.48234 * wavelength        # Typically 0.5 * wavelength
    base_director_length = 0.45507 * wavelength    # Typically 0.4 * wavelength

    # Spacing between elements as a fraction of the wavelength
    reflector_spacing = 0.2 * wavelength       # Typically 0.2 * wavelength
    director_spacing = 0.3 * wavelength        # Typically 0.3 * wavelength

    # Calculate individual director lengths (can be slightly shorter for later directors)
    director_lengths = [
        base_director_length - 0.004295 * i * wavelength  # Slightly taper lengths
        for i in range(num_directors)
    ]

    # Create a list of director spacings
    director_spacings = [(i + 1) * director_spacing for i in range(num_directors)]

    dimensions = {
        # "wavelength (m)": wavelength,
        # "driven_element_length (m)": driven_element_length,
        "reflector_length (m)": reflector_length,
        "director_lengths (m)": director_lengths,
        # "reflector_spacing (m)": reflector_spacing,
        # "director_spacings (m)": director_spacings,
        # "boom_diameter (m)": boom_diameter,
        # "wire_diameter (m)": wire_diameter,
    }

    return dimensions

# Example usage
frequency = 144  # Frequency in MHz (e.g., 144 MHz for 2-meter band)
num_directors = 5  # Number of directors
boom_diameter = 0.02  # Diameter of the boom in meters (e.g., 2 cm)
wire_diameter = 0.004  # Diameter of the wire in meters (e.g., 3 mm)

dimensions = yagi_antenna_dimensions(frequency, num_directors, boom_diameter, wire_diameter)

for key, value in dimensions.items():
    print(f"{key}: {value}")

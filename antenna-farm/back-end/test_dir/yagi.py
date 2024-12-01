import math

def yagi_uda_design(
    frequency,
    element_diameter,
    boom_diameter,
    num_directors,
    material_type="aluminum",
    material_velocity_factor=1.0
):
    """
    Calculate the effective element lengths and gain of a Yagi-Uda antenna, considering material type.

    Parameters:
        frequency (float): Operating frequency in Hz.
        element_diameter (float): Diameter of the elements in meters.
        boom_diameter (float): Diameter of the boom in meters.
        num_directors (int): Number of director elements.
        material_type (str): Material type of the elements ("copper" or "aluminum").
        material_velocity_factor (float): Velocity factor of the material (default=1.0 for air).

    Returns:
        dict: A dictionary containing calculated lengths, spacings, and estimated gain.
    """
    # Speed of light
    c = 3e8  # m/s

    # Conductivity of materials (in S/m)
    conductivity = {
        "copper": 5.8e7,  # Copper conductivity
        "aluminum": 3.8e7  # Aluminum conductivity
    }

    if material_type.lower() not in conductivity:
        raise ValueError("Invalid material type. Choose 'copper' or 'aluminum'.")

    # Material efficiency factor (relative to copper)
    material_efficiency = conductivity[material_type.lower()] / conductivity["copper"]

    # Wavelength
    wavelength = c / (frequency * math.sqrt(material_velocity_factor))

    # Correction factor for boom width effects (empirical)
    k = 0.4  # Adjust empirically or through simulation
    correction_factor = 1 - k * (boom_diameter / element_diameter)

    # Ensure the correction factor is realistic
    correction_factor = max(0.5, correction_factor)  # Clip at a minimum of 0.5 to avoid negative lengths

    # Driven element (resonant length)
    driven_length = wavelength / 2
    driven_length_eff = driven_length * correction_factor

    # Reflector length (5% longer than driven element)
    reflector_length = driven_length * 1.05
    reflector_length_eff = reflector_length * correction_factor

    # Director lengths (5% shorter than driven element, typically)
    director_length_base = driven_length * 0.95
    director_lengths = [
        director_length_base * correction_factor * (0.98 ** i)
        for i in range(num_directors)
    ]

    # Element spacing
    reflector_spacing = 0.2 * wavelength  # Reflector to driven
    director_spacing = 0.15 * wavelength  # Driven to first director (general assumption)

    # Gain approximation, adjusted for material efficiency
    gain = 4.8 + 10 * math.log10(num_directors) - k * boom_diameter / element_diameter
    gain *= material_efficiency  # Adjust gain based on material efficiency

    # Return the results as a dictionary
    return {
        "material_type": material_type,
        "wavelength": wavelength,
        "driven_length_eff": driven_length_eff,
        "reflector_length_eff": reflector_length_eff,
        "director_lengths_eff": director_lengths,
        "reflector_spacing": reflector_spacing,
        "director_spacing": director_spacing,
        "estimated_gain_dB": gain
    }

# Example usage
design_params = yagi_uda_design(
    frequency=145e6,  # 145 MHz
    element_diameter=0.01,  # 1 cm
    boom_diameter=0.05,  # 5 cm
    num_directors=5,  # 5 directors
    material_type="copper",  # Copper elements
    material_velocity_factor=1.0  # Air (default)
)

# Print the results
for key, value in design_params.items():
    if isinstance(value, list):
        print(f"{key}: {[f'{v:.4f}' for v in value]}")
    else:
        print(f"{key}: {value:.4f}" if isinstance(value, float) else f"{key}: {value}")

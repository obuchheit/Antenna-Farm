import math

def yagi_uda_dimensions(frequency, num_directors, wire_diameter, boom_diameter, wire_material, boom_material):
    """
    Calculate the dimensions and approximate gain of a Yagi-Uda antenna using various gain estimation formulas.

    Parameters:
        frequency (float): Frequency in Hz.
        num_directors (int): Number of director elements.
        wire_diameter (float): Diameter of the driven element wire in meters.
        boom_diameter (float): Diameter of the boom in meters.
        wire_material (str): Material of the driven element wire ('copper' or 'aluminum').
        boom_material (str): Material of the boom ('wood', 'pvc', or 'aluminum').

    Returns:
        None. Prints the calculated dimensions and approximate gain.
    """
    # Validate inputs
    wire_materials = ['copper', 'aluminum']
    boom_materials = ['wood', 'pvc', 'aluminum']

    if wire_material.lower() not in wire_materials:
        raise ValueError(f"Invalid wire material. Choose from: {wire_materials}.")
    if boom_material.lower() not in boom_materials:
        raise ValueError(f"Invalid boom material. Choose from: {boom_materials}.")

    if num_directors < 1:
        raise ValueError("Number of directors must be at least 1.")

    # Speed of light (m/s)
    c = 3e8

    # Wavelength
    wavelength = c / frequency

    # Adjusted factor for driver length based on empirical design
    driver_length = 0.475 * wavelength  # Approximately 95% of the half-wavelength
    
    # Reflector
    reflector_length = 0.485 * wavelength  # Reflector is slightly longer than the driver
    reflector_distance = 0.2 * wavelength  # Typically 0.2λ to 0.25λ behind the driver
    
    # Directors
    director_lengths = []
    director_spacing = []
    length_reduction_factor = 0.45 / num_directors  # Progressive shortening of directors

    for i in range(1, num_directors + 1):
        director_length = driver_length - (i * length_reduction_factor * wavelength)
        director_lengths.append(director_length)
        director_spacing.append(i * 0.15 * wavelength)  # Typical spacing between directors

    # Gain Estimations
    num_elements = num_directors + 2  # Directors + driver + reflector

    vk3auu_gain = 3.39 * math.log((num_elements - 1) * 0.2) + 9.15
    ring_gain = 10 * math.log10(5.4075 * ((num_elements - 1) * 0.2) + 4.25)
    bertelsmaier_gain = 7.773 * math.log10(num_elements - 1) + 9.28
    rothammel_gain = 3.39 * math.log(num_elements - 1) + 9.15

    # Print results
    print(f"Driver Length: {driver_length:.4f} m")
    print(f"Reflector Length: {reflector_length:.4f} m")
    print(f"Reflector Distance from Driver: {reflector_distance:.4f} m")
    print("Directors:")
    for i, (length, spacing) in enumerate(zip(director_lengths, director_spacing), start=1):
        print(f"  Director {i}: Length = {length:.4f} m, Spacing = {spacing:.4f} m")

    print("\nGain Estimations (in dBi):")
    print(f"  VK3AUU Method: {vk3auu_gain:.2f}")
    print(f"  Ring WA2PHW Method: {ring_gain:.2f}")
    print(f"  Bertelsmaier DBJ9BV Method: {bertelsmaier_gain:.2f}")
    print(f"  Rothammel Method: {rothammel_gain:.2f}")

    print("\nMaterial Considerations:")
    print(f"  Wire Material: {wire_material.capitalize()}")
    print(f"  Boom Material: {boom_material.capitalize()}")

# Example Usage
yagi_uda_dimensions(
    frequency=144e6,  # Frequency: 144 MHz
    num_directors=5,
    wire_diameter=0.004,  # 5 mm
    boom_diameter=0.02,   # 20 mm
    wire_material="copper",
    boom_material="aluminum"
)

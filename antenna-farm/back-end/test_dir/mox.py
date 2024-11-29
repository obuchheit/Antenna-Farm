import math

def moxon(dw, wl):
    d1 = 0.4342945 * math.log(dw)
    if d1 < -6:
        note = "Wire diameter too small, results uncertain"
    elif d1 > -2:
        note = "Wire diameter too large, results uncertain"
    else:
        note = None

    a = -0.0008571428571 * (d1 * d1) - 0.009571428571 * d1 + 0.3398571429
    b = -0.002142857143 * (d1 * d1) - 0.02035714286 * d1 + 0.008285714286
    c = 0.001809523381 * (d1 * d1) + 0.01780952381 * d1 + 0.05164285714
    d = 0.001 * d1 + 0.07178571429

    # Convert from mm to meters and feet
    a_m = a * wl / 1000  # in meters
    b_m = b * wl / 1000  # in meters
    c_m = c * wl / 1000  # in meters
    d_m = d * wl / 1000  # in meters

    a_ft = a_m * 3.28084  # in feet
    b_ft = b_m * 3.28084  # in feet
    c_ft = c_m * 3.28084  # in feet
    d_ft = d_m * 3.28084  # in feet

    return {
        'a_m': round(a_m, 3),
        'b_m': round(b_m, 3),
        'c_m': round(c_m, 3),
        'd_m': round(d_m, 3),
        'a_ft': round(a_ft, 3),
        'b_ft': round(b_ft, 3),
        'c_ft': round(c_ft, 3),
        'd_ft': round(d_ft, 3),
        'note': note
    }

def main():
    # Sample frequency (MHz) and wire diameter (mm)
    frequency = 146.0  # Example frequency
    wd = 2.05          # Example wire diameter

    # Calculate wavelength (in meters)
    wl = 299792.5 / frequency

    # Normalize the wire diameter based on wavelength
    dw = wd / wl

    # Get the calculated elements
    result = moxon(dw, wl)

    # Print the result elements
    print("Moxon Antenna Dimensions:")
    print(f"A (meters): {result['a_m']}, A (feet): {result['a_ft']}")
    print(f"B (meters): {result['b_m']}, B (feet): {result['b_ft']}")
    print(f"C (meters): {result['c_m']}, C (feet): {result['c_ft']}")
    print(f"D (meters): {result['d_m']}, D (feet): {result['d_ft']}")
    if result['note']:
        print(f"Note: {result['note']}")

if __name__ == '__main__':
    main()

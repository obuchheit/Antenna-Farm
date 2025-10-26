# Antenna Calculator

Cross-platform antenna design calculator for amateur radio. Calculate dimensions for Yagi-Uda and Moxon Rectangle antennas using proven design methods.

## Features

### Yagi-Uda Antenna (DL6WU Method)
- Optimized spacing algorithm (non-uniform for maximum gain)
- Variable element count (3+ elements)
- Boom correction factors for different mounting methods
- Wire and boom diameter corrections

### Moxon Rectangle Antenna (L.B. Cebik Polynomials)
- High-precision polynomial-based calculations
- Wire diameter range validation
- Compact directional antenna design

### User Interface
- Tabbed interface (Yagi / Moxon / About)
- Metric and Imperial unit support
- Color-coded results display
- Input validation

## Installation & Usage

### macOS / Linux (Command Line)

```bash
cd antenna-calculator

# Install dependencies
pip3 install -r requirements.txt

# Run directly (main.py is executable)
./main.py

# Or use make
make run
```

### Windows

**Option 1: Run from Source**
```bash
pip install -r requirements.txt
python main.py
```

**Option 2: Build Executable with Icon**
```bash
# Generate icons first
python create_icons.py

# Build standalone .exe
pip install pyinstaller
make windows

# Run: dist\AntennaCalculator.exe
```

### Android

```bash
# Install Buildozer
pip3 install buildozer

# Generate icons
make icons

# Build APK
make android

# Install: adb install bin/antennacalc-1.0-debug.apk
```

### iOS

```bash
# Requires macOS with Xcode
pip3 install buildozer

# Generate icons
make icons

# Build IPA
make ios
```

## Icon Generation

Icons are generated for mobile platforms (Android/iOS) and Windows only. macOS and Linux run the app directly via command line.

```bash
# Generate icons for Android, iOS, and Windows
make icons
```

This creates:
- **Android**: `assets/icon.png` (512x512) + density-specific icons
- **iOS**: 18 icon sizes (29x29 to 1024x1024)
- **Windows**: `assets/icon.ico` (multi-resolution)

## Quick Reference

```bash
# Common commands
make help          # Show all available commands
make install       # Install dependencies
make run           # Run the app (macOS/Linux)
make clean         # Clean build artifacts
make check         # Check installed dependencies

# Mobile builds
make android       # Build Android APK
make ios           # Build iOS IPA

# Windows build
make windows       # Build Windows executable

# Icon generation
make icons         # Generate mobile & Windows icons
```

## Platform-Specific Notes

### macOS / Linux
- Run directly with `./main.py` or `python3 main.py`
- No executable or installer needed
- No desktop icons (run from terminal)

### Windows
- Build standalone `.exe` with icon using PyInstaller
- Icon appears in File Explorer and taskbar

### Android / iOS
- Full app icons on home screen
- Configured via `buildozer.spec`

## Technical Details

### DL6WU Yagi Algorithm

Optimized for VHF/UHF frequencies with non-uniform element spacing:

**Spacing sequence** (as fractions of wavelength):
```
0.075λ, 0.18λ, 0.215λ, 0.25λ, 0.28λ, 0.3λ, 0.315λ, 0.33λ,
0.345λ, 0.36λ, 0.375λ, 0.385λ, 0.39λ, 0.395λ, then 0.4λ
```

**Scaling factors:**
- Director length: 97.775% of driven element
- Reflector length: 105% of driven element

**Boom corrections:**
- Center connected: 98%
- Isolated above: 97%
- Insulated boom: 100%

### L.B. Cebik Moxon Polynomials

High-precision equations based on NEC modeling:

1. Normalize wire diameter: `dw = wire_diameter / wavelength`
2. Calculate: `d1 = 0.4342945 × ln(dw)`
3. Apply polynomial equations for A, B, C, D dimensions
4. Scale by wavelength

**Valid range**: `-6 < d1 < -2` (approx. 0.25mm to 6mm wire at 2m band)

## Project Structure

```
antenna-calculator/
├── main.py              # Executable Kivy app
├── create_icons.py      # Icon generation script
├── requirements.txt     # Python dependencies
├── buildozer.spec       # Mobile build config
├── Makefile            # Build automation
├── README.md           # This file
├── .gitignore          # Git ignore patterns
├── assets/             # Icons
│   ├── icon_source.svg # SVG source
│   ├── icon.png        # Android icon
│   ├── icon.ico        # Windows icon
│   └── icon_ios_*.png  # iOS icons
└── tests/              # Unit tests
```

## Dependencies

- **Python**: 3.8+
- **Kivy**: 2.2.0
- **KivyMD**: 1.1.1 (optional)
- **Buildozer**: For mobile builds
- **PyInstaller**: For Windows executable

## License

Open source - MIT License

## Credits

- **DL6WU**: Günter Hoch - Optimized Yagi design method
- **L.B. Cebik (SK)**: Moxon polynomial equations
- **Kivy Framework**: Cross-platform development

## Support

- **Issues**: [GitHub Issues](https://github.com/antenna-calculator/issues)
- **Email**: info@hamradiotools.org

## Disclaimer

These calculations are design guidelines. Actual antenna performance depends on construction quality, environment, and installation. Always verify designs with antenna modeling software (NEC2, EZNEC, 4NEC2) before building.

---

**73!**

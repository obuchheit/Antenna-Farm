# Antenna Calculator

Cross-platform antenna design calculator for amateur radio enthusiasts. Calculate dimensions for Yagi-Uda and Moxon Rectangle antennas with high precision using proven design methods.

## Features

### Yagi-Uda Antenna (DL6WU Method)
- **Optimized Spacing Algorithm**: Non-uniform element spacing for maximum gain
- **Variable Element Count**: Support for 3+ elements
- **Boom Correction Factors**: Accurate corrections for different mounting methods
- **Multiple Mounting Types**: Center connected, isolated above, insulated boom
- **Diameter Corrections**: Accounts for wire and boom diameter

### Moxon Rectangle Antenna (L.B. Cebik Polynomials)
- **High Precision**: Polynomial-based calculations from L.B. Cebik's research
- **Wire Diameter Range Checking**: Validates inputs for accuracy
- **Compact Design**: Ideal for limited space installations
- **Easy to Build**: Simple rectangular construction

### User Interface
- **Tabbed Interface**: Easy navigation between calculators
- **Unit Flexibility**: Metric (meters) and Imperial (feet) units
- **Color-Coded Results**: Enhanced readability with markup formatting
- **Input Validation**: Real-time error checking
- **Responsive Design**: Works on phones, tablets, and desktop

## Platform Support

- **Android** (API 21+)
- **iOS** (10.0+)
- **Windows** (7+)
- **macOS** (10.12+)
- **Linux** (Ubuntu 18.04+, Fedora 30+)

## Installation

### Quick Start

Before building the app, you need to generate the icon files:

```bash
# Generate all platform icons from SVG source
make icons

# On macOS, also create .icns file
make macos-icon
```

This will create icons in multiple formats for Android, iOS, Windows, macOS, and Linux.

### Desktop (Windows, macOS, Linux)

#### Option 1: Run from Source
```bash
# Clone or download the repository
cd antenna-calculator

# Install dependencies
pip install -r requirements.txt

# Run the application
python main.py
```

#### Option 2: Using Make
```bash
make install
make run
```

#### Option 3: Install as Package
```bash
pip install .
antenna-calculator
```

#### Option 4: Install with Desktop Shortcut (Linux)
```bash
make icons              # Generate icons first
make linux-install      # Build and install with menu entry
# Now find "Antenna Calculator" in your applications menu
```

### Android

#### Option 1: Build from Source
```bash
# Install Buildozer
pip install buildozer

# Build APK (first build takes 30+ minutes)
make android

# APK will be in: bin/antennacalc-1.0-debug.apk
# Transfer to your Android device and install
```

#### Option 2: Download Pre-built APK
Download the latest APK from the [Releases](https://github.com/antenna-calculator/releases) page.

### iOS

```bash
# Requires macOS with Xcode
pip install buildozer
make ios

# IPA will be in: bin/
```

## Usage

### Yagi-Uda Calculator

1. Select the **Yagi (DL6WU)** tab
2. Enter your parameters:
   - **Frequency**: Operating frequency (with unit selector)
   - **Elements**: Number of elements (minimum 3)
   - **Wire Diameter**: Element wire diameter in mm
   - **Boom Diameter**: Boom diameter in mm
   - **Boom Relation**: Mounting method
     - `center_connected`: Elements mounted directly to conductive boom
     - `isolated_above`: Elements mounted above boom with insulators
     - `insulated_boom`: Non-conductive boom material
   - **Display Units**: Choose metric or imperial output
3. Press **Calculate**
4. View results:
   - Element lengths (reflector, driven element, directors)
   - Spacing from reflector for each element
   - Total boom length

### Moxon Rectangle Calculator

1. Select the **Moxon (Cebik)** tab
2. Enter your parameters:
   - **Frequency**: Operating frequency (with unit selector)
   - **Wire Diameter**: Wire diameter in mm
   - **Display Units**: Metric, Imperial, or Both
3. Press **Calculate**
4. View results:
   - **A**: Element half-length
   - **B**: Tail length
   - **C**: Tail spacing
   - **D**: Element spacing

The calculator will warn you if wire diameter is outside the optimal range.

## Building for Distribution

### Desktop Executables

#### Windows
```bash
# Generate icons first
make icons

# Build standalone executable with icon
pip install pyinstaller
make windows
# Output: dist/AntennaCalculator.exe (with icon)

# Optional: Create installer with desktop shortcut
# Requires NSIS (https://nsis.sourceforge.io/)
make windows-installer
# Output: dist/AntennaCalculator-Setup.exe
```

The Windows installer will:
- Install the app to Program Files
- Create Start Menu shortcut with icon
- Create Desktop shortcut with icon
- Add uninstaller

#### macOS
```bash
# Generate icons first
make icons
make macos-icon  # Creates .icns file

# Build standalone app with icon
pip install pyinstaller
make macos
# Output: dist/AntennaCalculator.app (with icon)
```

The macOS app bundle will have a proper icon in Finder and Dock.

#### Linux
```bash
# Generate icons first
make icons

# Build standalone executable
pip install pyinstaller
make linux
# Output: dist/antenna-calculator

# Or install system-wide with desktop entry
make linux-install
# Creates menu entry with icon in Applications menu
```

The Linux installation will:
- Install to `/usr/local/bin/antenna-calculator`
- Create desktop entry in `/usr/share/applications/`
- Add icon to `/usr/local/share/icons/`
- Appear in your applications menu with icon

### Mobile Apps

Both Android and iOS builds will automatically use the icons specified in `buildozer.spec`.

#### Android Release Build
```bash
# Icons are automatically included from assets/icon.png
make icons              # Generate icons first
make android-release    # Build release APK
# Sign the APK before distribution
```

The Android APK will have the app icon on the home screen and app drawer.

#### iOS Release Build
```bash
# Icons are automatically included from assets/icon_ios_1024.png
make icons              # Generate icons first
make ios                # Build IPA
# Requires Apple Developer account for signing
```

The iOS app will have the icon on the home screen and in the App Store.

## Technical Details

### DL6WU Yagi Algorithm

The DL6WU method is a well-established design for long-boom Yagi antennas, optimized for VHF/UHF frequencies. Key features:

- **Non-uniform Spacing**: Element spacing increases toward the rear for optimum performance
- **Scaling Factors**:
  - Director length: 97.775% of driven element
  - Reflector length: 105% of driven element
- **Boom Corrections**:
  - Center connected: 98% factor
  - Isolated above: 97% factor
  - Insulated boom: 100% (no correction)
- **Diameter Corrections**: Subtracts (wire_diameter + boom_diameter) × 0.5

Spacing sequence (as fractions of wavelength):
```
0.075λ, 0.18λ, 0.215λ, 0.25λ, 0.28λ, 0.3λ, 0.315λ, 0.33λ,
0.345λ, 0.36λ, 0.375λ, 0.385λ, 0.39λ, 0.395λ, then 0.4λ
```

### L.B. Cebik Moxon Polynomials

L.B. Cebik (SK) developed high-precision polynomial equations for Moxon rectangles based on extensive NEC modeling. The calculations:

1. Normalize wire diameter: `dw = wire_diameter / wavelength`
2. Calculate logarithmic term: `d1 = 0.4342945 × ln(dw)`
3. Apply polynomial equations for each dimension:
   - **A coefficient**: `-0.0008571428571×d1² - 0.009571428571×d1 + 0.3398571429`
   - **B coefficient**: `-0.002142857143×d1² - 0.02035714286×d1 + 0.008285714286`
   - **C coefficient**: `0.001809523381×d1² + 0.01780952381×d1 + 0.05164285714`
   - **D coefficient**: `0.001×d1 + 0.07178571429`
4. Scale by wavelength to get physical dimensions

**Valid range**: `-6 < d1 < -2` (approximately 0.25mm to 6mm wire diameter at 2m band)

### Calculation Accuracy

- **Yagi**: Optimized for 50-1000 MHz, 3-20 elements
- **Moxon**: Most accurate for wire diameters in valid range
- Both methods use speed of light: 299,792,458 m/s

## Development

### Project Structure
```
antenna-calculator/
├── main.py                      # Main application file
├── create_icons.py              # Icon generation script
├── requirements.txt             # Python dependencies
├── buildozer.spec               # Mobile build configuration
├── setup.py                     # Desktop installation script
├── Makefile                     # Build automation
├── README.md                    # This file
├── .gitignore                   # Git ignore patterns
├── antenna-calculator.desktop   # Linux desktop entry
├── installer.nsi                # Windows NSIS installer script
├── assets/                      # Images and icons
│   ├── icon_source.svg         # Source SVG icon
│   ├── icon.png                # Main icon (512x512)
│   ├── icon.ico                # Windows icon
│   ├── icon.icns               # macOS icon
│   ├── icon.iconset/           # macOS iconset folder
│   └── icon_*.png              # Various size icons
├── tests/                       # Unit tests
└── docs/                        # Additional documentation
```

### Icon Generation

The app includes a comprehensive icon generation system:

```bash
# Generate all icons from SVG source
make icons
```

This creates:
- **Android**: `icon.png` (512x512) and density-specific icons
- **iOS**: Multiple sizes from 29x29 to 1024x1024
- **Windows**: `icon.ico` (multi-resolution)
- **macOS**: `icon.iconset/` folder (run `make macos-icon` to create `.icns`)
- **Linux**: PNG icons in various sizes

**Customizing the Icon:**
1. Edit `assets/icon_source.svg` with your design
2. Or replace `assets/icon_base.png` with a 1024x1024 PNG
3. Run `make icons` to regenerate all formats

### Running Tests
```bash
make test
```

### Development Mode
```bash
make dev
```

### Checking Dependencies
```bash
make check
```

## Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is open source and available under the MIT License.

## Credits

- **DL6WU**: Günter Hoch, for the optimized Yagi design method
- **L.B. Cebik (SK)**: For extensive antenna modeling and Moxon polynomial equations
- **Kivy Framework**: For cross-platform development capabilities

## Support

- **Issues**: [GitHub Issues](https://github.com/antenna-calculator/issues)
- **Documentation**: [Project Wiki](https://github.com/antenna-calculator/wiki)
- **Email**: info@hamradiotools.org

## Disclaimer

These calculations are provided as design guidelines. Actual antenna performance depends on many factors including construction quality, local environment, and installation height. Always verify designs with antenna modeling software (NEC2, EZNEC, 4NEC2) before building.

## Version History

### 1.0.0 (2024)
- Initial release
- DL6WU Yagi calculator with optimized spacing
- L.B. Cebik Moxon calculator
- Cross-platform support (Android, iOS, Windows, macOS, Linux)
- Material Design UI
- Metric and Imperial units

---

**73 de Antenna Calculator Team**

*Made with ❤️ for the amateur radio community*

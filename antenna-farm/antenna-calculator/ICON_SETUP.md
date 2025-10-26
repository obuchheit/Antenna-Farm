# Icon and Shortcut Setup Guide

This guide explains how to add icons and create shortcuts/executable icons for the Antenna Calculator app across all platforms.

## Quick Start

```bash
# 1. Generate all platform icons
make icons

# 2. On macOS, also create .icns file
make macos-icon  # (macOS only)
```

## What Gets Created

The icon generation system creates icons for all platforms:

### Android
- `assets/icon.png` (512x512) - Main app icon
- `assets/icon_mdpi.png` (48x48)
- `assets/icon_hdpi.png` (72x72)
- `assets/icon_xhdpi.png` (96x96)
- `assets/icon_xxhdpi.png` (144x144)
- `assets/icon_xxxhdpi.png` (192x192)

**Icon Location**: Configured in `buildozer.spec`
```ini
icon.filename = %(source.dir)s/assets/icon.png
```

**Result**: App icon appears on home screen and app drawer

### iOS
- `assets/icon_ios_29.png` through `assets/icon_ios_1024.png`
- All sizes required by Apple App Store

**Icon Location**: Configured in `buildozer.spec` under `[app:ios]`
```ini
icon.filename = %(source.dir)s/assets/icon_ios_1024.png
```

**Result**: App icon appears on home screen and in App Store

### Windows
- `assets/icon.ico` - Multi-resolution icon (16, 24, 32, 48, 64, 128, 256)

**Usage**:
1. PyInstaller executable: Specified in Makefile
   ```makefile
   --icon=assets/icon.ico
   ```
2. NSIS installer: Creates desktop and Start Menu shortcuts
   ```nsis
   CreateShortCut "$DESKTOP\${APP_NAME}.lnk" "$INSTDIR\${MAIN_APP_EXE}" "" "$INSTDIR\icon.ico"
   ```

**Result**:
- Executable has icon in File Explorer
- Desktop shortcut with icon
- Start Menu entry with icon

### macOS
- `assets/icon.iconset/` - Folder with all required sizes
- `assets/icon.icns` - macOS icon bundle (created by `make macos-icon`)

**Usage**: PyInstaller app bundle specified in Makefile
```makefile
--icon=assets/icon.icns
```

**Result**: App icon appears in Finder, Dock, and Launchpad

### Linux
- `assets/icon_16.png` through `assets/icon_1024.png`
- Multiple sizes for different contexts

**Usage**: Desktop entry file
```desktop
Icon=/usr/local/share/icons/antenna-calculator.png
```

**Result**: App icon appears in applications menu

## Platform-Specific Instructions

### Android

```bash
# 1. Generate icons
make icons

# 2. Build APK (icon automatically included)
make android

# 3. Install on device
adb install bin/antennacalc-1.0-debug.apk
```

The icon will appear on your home screen.

### iOS

```bash
# 1. Generate icons
make icons

# 2. Build IPA (icon automatically included)
make ios

# 3. Submit to App Store or install via TestFlight
```

The icon will appear on the home screen.

### Windows

**Option 1: Standalone Executable**
```bash
# 1. Generate icons
make icons

# 2. Build executable with icon
make windows
# Creates: dist/AntennaCalculator.exe
```

The .exe file will have the icon visible in File Explorer.

**Option 2: Installer with Shortcuts**
```bash
# 1. Generate icons
make icons

# 2. Build installer (requires NSIS)
make windows-installer
# Creates: dist/AntennaCalculator-Setup.exe

# 3. Run the installer
```

The installer creates:
- Desktop shortcut with icon
- Start Menu entry with icon
- Uninstaller in Control Panel

### macOS

```bash
# 1. Generate icons
make icons

# 2. Create .icns file
make macos-icon

# 3. Build app bundle
make macos
# Creates: dist/AntennaCalculator.app

# 4. Move to Applications folder
cp -r dist/AntennaCalculator.app /Applications/
```

The app will have the icon in Finder, Dock, and Launchpad.

### Linux

**Option 1: Standalone Executable**
```bash
# 1. Generate icons
make icons

# 2. Build executable
make linux
# Creates: dist/antenna-calculator
```

**Option 2: System Installation with Menu Entry**
```bash
# 1. Generate icons
make icons

# 2. Install system-wide
make linux-install
```

This installs:
- Executable to `/usr/local/bin/antenna-calculator/`
- Icon to `/usr/local/share/icons/antenna-calculator.png`
- Desktop entry to `/usr/share/applications/antenna-calculator.desktop`

The app will appear in your applications menu (GNOME, KDE, etc.) with the icon.

**To uninstall:**
```bash
make linux-uninstall
```

## Customizing the Icon

### Option 1: Edit the SVG (Recommended)

1. Open `assets/icon_source.svg` in a vector editor (Inkscape, Illustrator)
2. Modify the design
3. Save the SVG
4. Run `make icons` to regenerate all formats

### Option 2: Replace with PNG

1. Create a 1024x1024 PNG icon
2. Save as `assets/icon_base.png`
3. Run `make icons` to generate all sizes

### Option 3: Manual Icon Files

If you have pre-made icons, place them in `assets/`:
- `icon.png` (512x512 or larger) - Android/general
- `icon.ico` - Windows
- `icon.icns` - macOS
- `icon_ios_1024.png` - iOS

## Icon Generation Script

The `create_icons.py` script handles all conversions:

```python
# Requires: pip install Pillow

# Optional (for SVG conversion):
# pip install cairosvg
# or use Inkscape CLI
```

**What it does:**
1. Converts SVG to base PNG (1024x1024)
2. Resizes to all required sizes for each platform
3. Creates Windows .ico (multi-resolution)
4. Creates macOS .iconset folder
5. Generates density-specific Android icons

## Troubleshooting

### SVG Not Converting

If `make icons` can't convert the SVG:

1. Install cairosvg: `pip install cairosvg`
2. Or install Inkscape: https://inkscape.org/
3. Or manually convert SVG to PNG (1024x1024) and save as `assets/icon_base.png`

### macOS .icns Not Created

Run manually:
```bash
iconutil -c icns assets/icon.iconset -o assets/icon.icns
```

Requires macOS 10.7+

### Linux Icon Not Showing

Update icon cache:
```bash
sudo gtk-update-icon-cache /usr/local/share/icons/
```

### Windows Installer Fails

Install NSIS from https://nsis.sourceforge.io/ and ensure it's in your PATH.

## Icon Specifications

### Android
- Format: PNG
- Sizes: 48, 72, 96, 144, 192 px
- Main: 512x512 px

### iOS
- Format: PNG (no transparency)
- Sizes: 29, 40, 50, 57, 58, 60, 72, 76, 80, 87, 100, 114, 120, 144, 152, 167, 180, 1024 px

### Windows
- Format: ICO (multi-resolution)
- Sizes: 16, 24, 32, 48, 64, 128, 256 px

### macOS
- Format: ICNS
- Sizes: 16, 32, 64, 128, 256, 512, 1024 px (with @2x retina variants)

### Linux
- Format: PNG
- Recommended: 512x512 or larger
- Common sizes: 16, 24, 32, 48, 64, 128, 256, 512 px

## Files Reference

- `assets/icon_source.svg` - Source vector icon
- `create_icons.py` - Icon generation script
- `buildozer.spec` - Mobile icon configuration
- `antenna-calculator.desktop` - Linux desktop entry
- `installer.nsi` - Windows installer with icon shortcuts
- `Makefile` - Build commands including icon generation

## Summary

The complete icon setup process:

```bash
# One-time setup
make icons                  # Generate all icons
make macos-icon            # macOS only

# Then build for your platform
make android               # Android with icon
make ios                   # iOS with icon
make windows               # Windows .exe with icon
make windows-installer     # Windows installer with shortcuts
make macos                 # macOS .app with icon
make linux-install         # Linux with menu entry
```

All platforms will have proper icons in their native locations!

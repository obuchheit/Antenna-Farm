#!/usr/bin/env python3
"""
Icon generation script for Antenna Calculator
Generates icons in all required formats for different platforms
"""

import os
import sys

def create_icons():
    """Generate icons for all platforms"""

    # Check if PIL/Pillow is available
    try:
        from PIL import Image
    except ImportError:
        print("Pillow not found. Installing...")
        os.system(f"{sys.executable} -m pip install Pillow")
        from PIL import Image

    # Icon sizes for different platforms
    sizes = {
        'android': [
            (48, 'mdpi'),
            (72, 'hdpi'),
            (96, 'xhdpi'),
            (144, 'xxhdpi'),
            (192, 'xxxhdpi'),
        ],
        'ios': [29, 40, 50, 57, 58, 60, 72, 76, 80, 87, 100, 114, 120, 144, 152, 167, 180, 1024],
        'desktop': [16, 24, 32, 48, 64, 128, 256, 512, 1024],
    }

    assets_dir = 'assets'
    source_svg = os.path.join(assets_dir, 'icon_source.svg')

    # Check if we need to convert SVG to PNG first
    if os.path.exists(source_svg):
        print("Converting SVG to base PNG...")
        try:
            # Try using cairosvg if available
            import cairosvg
            base_png = os.path.join(assets_dir, 'icon_base.png')
            cairosvg.svg2png(url=source_svg, write_to=base_png, output_width=1024, output_height=1024)
            print(f"Created base PNG: {base_png}")
        except ImportError:
            print("cairosvg not found. Trying Inkscape...")
            # Try using Inkscape command line
            base_png = os.path.join(assets_dir, 'icon_base.png')
            result = os.system(f'inkscape {source_svg} --export-type=png --export-filename={base_png} -w 1024 -h 1024')
            if result != 0:
                print("\nWARNING: Could not convert SVG automatically.")
                print("Please manually convert assets/icon_source.svg to assets/icon_base.png (1024x1024)")
                print("You can use: https://www.adobe.com/express/feature/image/convert/svg-to-png")
                print("or Inkscape: inkscape icon_source.svg --export-type=png --export-filename=icon_base.png -w 1024 -h 1024")
                return False
    else:
        base_png = os.path.join(assets_dir, 'icon_base.png')

    if not os.path.exists(base_png):
        print(f"\nERROR: Base icon not found at {base_png}")
        print("Please create a 1024x1024 PNG icon and save it as assets/icon_base.png")
        return False

    # Load base image
    print(f"Loading base image: {base_png}")
    base_img = Image.open(base_png)

    # Ensure it's square
    if base_img.size[0] != base_img.size[1]:
        print("Warning: Base image is not square, cropping to square...")
        min_size = min(base_img.size)
        base_img = base_img.crop((0, 0, min_size, min_size))

    # Generate Android icons
    print("\nGenerating Android icons...")
    for size, density in sizes['android']:
        img = base_img.resize((size, size), Image.Resampling.LANCZOS)
        filename = f'icon_{density}.png'
        filepath = os.path.join(assets_dir, filename)
        img.save(filepath, 'PNG')
        print(f"  Created {filename} ({size}x{size})")

    # Main Android icon
    main_icon = base_img.resize((512, 512), Image.Resampling.LANCZOS)
    main_icon.save(os.path.join(assets_dir, 'icon.png'), 'PNG')
    print(f"  Created icon.png (512x512) - main Android icon")

    # Generate iOS icons
    print("\nGenerating iOS icons...")
    for size in sizes['ios']:
        img = base_img.resize((size, size), Image.Resampling.LANCZOS)
        filename = f'icon_ios_{size}.png'
        filepath = os.path.join(assets_dir, filename)
        img.save(filepath, 'PNG')
        print(f"  Created {filename} ({size}x{size})")

    # Generate desktop icons
    print("\nGenerating desktop icons...")
    for size in sizes['desktop']:
        img = base_img.resize((size, size), Image.Resampling.LANCZOS)
        filename = f'icon_{size}.png'
        filepath = os.path.join(assets_dir, filename)
        img.save(filepath, 'PNG')
        print(f"  Created {filename} ({size}x{size})")

    # Create Windows ICO file (multi-resolution)
    print("\nCreating Windows .ico file...")
    ico_sizes = [(16, 16), (24, 24), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]
    ico_images = [base_img.resize(size, Image.Resampling.LANCZOS) for size in ico_sizes]
    ico_path = os.path.join(assets_dir, 'icon.ico')
    ico_images[0].save(ico_path, format='ICO', sizes=ico_sizes)
    print(f"  Created icon.ico (multi-resolution)")

    # Create macOS ICNS file (requires additional tools)
    print("\nFor macOS .icns file:")
    print("  On macOS, run: make macos-icon")
    print("  Or manually: iconutil -c icns assets/icon.iconset")

    # Create iconset folder for macOS
    iconset_dir = os.path.join(assets_dir, 'icon.iconset')
    os.makedirs(iconset_dir, exist_ok=True)

    mac_sizes = [16, 32, 64, 128, 256, 512, 1024]
    for size in mac_sizes:
        # Standard resolution
        img = base_img.resize((size, size), Image.Resampling.LANCZOS)
        img.save(os.path.join(iconset_dir, f'icon_{size}x{size}.png'), 'PNG')

        # Retina resolution (@2x)
        if size <= 512:
            img_2x = base_img.resize((size * 2, size * 2), Image.Resampling.LANCZOS)
            img_2x.save(os.path.join(iconset_dir, f'icon_{size}x{size}@2x.png'), 'PNG')

    print(f"  Created iconset folder: {iconset_dir}")

    print("\n✓ Icon generation complete!")
    print("\nGenerated files:")
    print(f"  - Android: assets/icon.png and icon_*.png")
    print(f"  - iOS: assets/icon_ios_*.png")
    print(f"  - Windows: assets/icon.ico")
    print(f"  - macOS: assets/icon.iconset/ (run 'iconutil' to create .icns)")
    print(f"  - Linux: assets/icon_*.png")

    return True

if __name__ == '__main__':
    success = create_icons()
    sys.exit(0 if success else 1)

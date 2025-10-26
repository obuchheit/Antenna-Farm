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

    # Icon sizes for mobile and Windows platforms only
    sizes = {
        'android': [
            (48, 'mdpi'),
            (72, 'hdpi'),
            (96, 'xhdpi'),
            (144, 'xxhdpi'),
            (192, 'xxxhdpi'),
        ],
        'ios': [29, 40, 50, 57, 58, 60, 72, 76, 80, 87, 100, 114, 120, 144, 152, 167, 180, 1024],
    }

    assets_dir = 'assets'
    source_svg = os.path.join(assets_dir, 'icon_source.svg')

    # Check if we need to convert SVG to PNG first
    base_png = os.path.join(assets_dir, 'icon_base.png')

    if os.path.exists(source_svg) and not os.path.exists(base_png):
        print("Converting SVG to base PNG...")
        converted = False

        # Try method 1: cairosvg
        try:
            import cairosvg
            cairosvg.svg2png(url=source_svg, write_to=base_png, output_width=1024, output_height=1024)
            print(f"✓ Created base PNG using cairosvg: {base_png}")
            converted = True
        except Exception as e:
            print(f"cairosvg not available: {e}")

        # Try method 2: Inkscape CLI
        if not converted:
            print("Trying Inkscape...")
            result = os.system(f'inkscape {source_svg} --export-type=png --export-filename={base_png} -w 1024 -h 1024 2>/dev/null')
            if result == 0:
                print(f"✓ Created base PNG using Inkscape: {base_png}")
                converted = True

        # Try method 3: svglib + reportlab
        if not converted:
            print("Trying svglib...")
            try:
                from svglib.svglib import svg2rlg
                from reportlab.graphics import renderPM
                drawing = svg2rlg(source_svg)
                renderPM.drawToFile(drawing, base_png, fmt='PNG', dpi=72, bg=0xffffff)
                # Resize to 1024x1024
                img = Image.open(base_png)
                img = img.resize((1024, 1024), Image.Resampling.LANCZOS)
                img.save(base_png, 'PNG')
                print(f"✓ Created base PNG using svglib: {base_png}")
                converted = True
            except Exception as e:
                print(f"svglib not available: {e}")

        # If nothing worked, provide manual instructions
        if not converted:
            print("\n" + "="*60)
            print("⚠️  Could not convert SVG automatically.")
            print("="*60)
            print("\nPlease convert manually using one of these options:")
            print("\n1. Online converter:")
            print("   https://www.adobe.com/express/feature/image/convert/svg-to-png")
            print("   https://cloudconvert.com/svg-to-png")
            print("\n2. Install Inkscape and run:")
            print(f"   inkscape {source_svg} --export-type=png --export-filename={base_png} -w 1024 -h 1024")
            print("\n3. Install Cairo library (for cairosvg):")
            print("   brew install cairo")
            print("   pip3 install cairosvg")
            print("\n4. Or simply create a 1024x1024 PNG manually and save as:")
            print(f"   {base_png}")
            print("="*60)
            return False

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

    # Create Windows ICO file (multi-resolution)
    print("\nCreating Windows .ico file...")
    ico_sizes = [(16, 16), (24, 24), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]
    ico_images = [base_img.resize(size, Image.Resampling.LANCZOS) for size in ico_sizes]
    ico_path = os.path.join(assets_dir, 'icon.ico')
    ico_images[0].save(ico_path, format='ICO', sizes=ico_sizes)
    print(f"  Created icon.ico (multi-resolution)")

    print("\n✓ Icon generation complete!")
    print("\nGenerated files:")
    print(f"  - Android: assets/icon.png and icon_*.png")
    print(f"  - iOS: assets/icon_ios_*.png")
    print(f"  - Windows: assets/icon.ico")
    print(f"\nNote: For macOS/Linux, run the app directly with: python3 main.py")

    return True

if __name__ == '__main__':
    success = create_icons()
    sys.exit(0 if success else 1)

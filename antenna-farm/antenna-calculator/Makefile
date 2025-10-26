.PHONY: help install run clean test android ios windows macos linux icons

help:
	@echo "Antenna Calculator Build System"
	@echo ""
	@echo "Available targets:"
	@echo "  make install       - Install dependencies"
	@echo "  make icons         - Generate all icon files"
	@echo "  make run           - Run the application"
	@echo "  make clean         - Clean build artifacts"
	@echo "  make test          - Run tests"
	@echo ""
	@echo "Platform-specific builds:"
	@echo "  make android       - Build Android APK"
	@echo "  make ios           - Build iOS IPA"
	@echo "  make windows       - Build Windows executable"
	@echo "  make macos         - Build macOS app"
	@echo "  make linux         - Build Linux executable"
	@echo "  make linux-install - Install on Linux system"
	@echo ""
	@echo "Icon generation:"
	@echo "  make icons         - Generate all platform icons"
	@echo "  make macos-icon    - Create macOS .icns file"

install:
	@echo "Installing dependencies..."
	pip3 install -r requirements.txt

run:
	@echo "Running Antenna Calculator..."
	python main.py

clean:
	@echo "Cleaning build artifacts..."
	rm -rf .buildozer
	rm -rf bin
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	@echo "Clean complete."

test:
	@echo "Running tests..."
	python3 -m pytest tests/ -v

# Android build using Buildozer
android:
	@echo "Building Android APK..."
	@which buildozer > /dev/null || (echo "Buildozer not found. Install with: pip install buildozer" && exit 1)
	buildozer android debug
	@echo "APK built: bin/*.apk"

android-release:
	@echo "Building Android APK (release)..."
	buildozer android release
	@echo "Release APK built: bin/*.apk"

# iOS build using Buildozer (requires macOS)
ios:
	@echo "Building iOS IPA..."
	@which buildozer > /dev/null || (echo "Buildozer not found. Install with: pip install buildozer" && exit 1)
	buildozer ios debug
	@echo "IPA built: bin/*.ipa"

# Windows build using PyInstaller
windows:
	@echo "Building Windows executable..."
	@which pyinstaller > /dev/null || (echo "PyInstaller not found. Install with: pip install pyinstaller" && exit 1)
	pyinstaller --name="AntennaCalculator" \
		--windowed \
		--onefile \
		--icon=assets/icon.ico \
		main.py
	@echo "Windows executable built: dist/AntennaCalculator.exe"

# macOS build using PyInstaller
macos:
	@echo "Building macOS app..."
	@which pyinstaller > /dev/null || (echo "PyInstaller not found. Install with: pip install pyinstaller" && exit 1)
	pyinstaller --name="AntennaCalculator" \
		--windowed \
		--onefile \
		--icon=assets/icon.icns \
		main.py
	@echo "macOS app built: dist/AntennaCalculator.app"

# Linux build using PyInstaller
linux:
	@echo "Building Linux executable..."
	@which pyinstaller > /dev/null || (echo "PyInstaller not found. Install with: pip install pyinstaller" && exit 1)
	pyinstaller --name="antenna-calculator" \
		--onefile \
		main.py
	@echo "Linux executable built: dist/antenna-calculator"

# Development server with auto-reload
dev:
	@echo "Running in development mode..."
	python main.py

# Install buildozer (for mobile builds)
install-buildozer:
	@echo "Installing Buildozer..."
	pip install buildozer
	pip install cython

# Install PyInstaller (for desktop builds)
install-pyinstaller:
	@echo "Installing PyInstaller..."
	pip install pyinstaller

# Full setup for development
setup-dev: install install-buildozer install-pyinstaller
	@echo "Development environment ready!"

# Check dependencies
check:
	@echo "Checking dependencies..."
	@python -c "import kivy; print(f'Kivy: {kivy.__version__}')" || echo "Kivy not installed"
	@python -c "import kivymd; print(f'KivyMD: {kivymd.__version__}')" || echo "KivyMD not installed"
	@which buildozer > /dev/null && echo "Buildozer: installed" || echo "Buildozer: not installed"
	@which pyinstaller > /dev/null && echo "PyInstaller: installed" || echo "PyInstaller: not installed"

# Icon generation
icons:
	@echo "Generating icons for all platforms..."
	python3 create_icons.py
	@echo "Icon generation complete!"

# macOS ICNS generation (requires macOS and iconutil)
macos-icon:
	@echo "Creating macOS .icns file..."
	@if [ -d "assets/icon.iconset" ]; then \
		iconutil -c icns assets/icon.iconset -o assets/icon.icns && \
		echo "✓ Created assets/icon.icns"; \
	else \
		echo "Error: assets/icon.iconset not found. Run 'make icons' first."; \
		exit 1; \
	fi

# Install on Linux system with desktop shortcut
linux-install: linux
	@echo "Installing Antenna Calculator on Linux..."
	sudo mkdir -p /usr/local/bin/antenna-calculator
	sudo cp -r * /usr/local/bin/antenna-calculator/
	sudo cp assets/icon_512.png /usr/local/share/icons/antenna-calculator.png
	sudo cp antenna-calculator.desktop /usr/share/applications/
	sudo chmod +x /usr/local/bin/antenna-calculator/main.py
	@echo "✓ Installed! Look for 'Antenna Calculator' in your applications menu."

# Uninstall from Linux
linux-uninstall:
	@echo "Uninstalling Antenna Calculator..."
	sudo rm -rf /usr/local/bin/antenna-calculator
	sudo rm -f /usr/local/share/icons/antenna-calculator.png
	sudo rm -f /usr/share/applications/antenna-calculator.desktop
	@echo "✓ Uninstalled."

# Create Windows installer (requires NSIS on Windows)
windows-installer: windows
	@echo "Creating Windows installer..."
	@which makensis > /dev/null || (echo "NSIS not found. Install from https://nsis.sourceforge.io/" && exit 1)
	makensis installer.nsi
	@echo "Installer created: dist/AntennaCalculator-Setup.exe"

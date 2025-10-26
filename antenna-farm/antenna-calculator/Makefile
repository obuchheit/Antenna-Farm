.PHONY: help install run clean test android ios windows icons

help:
	@echo "Antenna Calculator Build System"
	@echo ""
	@echo "Available targets:"
	@echo "  make install   - Install dependencies"
	@echo "  make run       - Run the application (macOS/Linux)"
	@echo "  make clean     - Clean build artifacts"
	@echo "  make test      - Run tests"
	@echo ""
	@echo "Mobile builds:"
	@echo "  make android   - Build Android APK"
	@echo "  make ios       - Build iOS IPA"
	@echo ""
	@echo "Windows build:"
	@echo "  make windows   - Build Windows executable"
	@echo ""
	@echo "Icon generation:"
	@echo "  make icons     - Generate mobile & Windows icons"

install:
	@echo "Installing dependencies..."
	pip3 install -r requirements.txt

run:
	@echo "Running Antenna Calculator..."
	./main.py

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
	@which buildozer > /dev/null || (echo "Buildozer not found. Install with: pip3 install buildozer" && exit 1)
	buildozer android debug
	@echo "APK built: bin/*.apk"

android-release:
	@echo "Building Android APK (release)..."
	buildozer android release
	@echo "Release APK built: bin/*.apk"

# iOS build using Buildozer (requires macOS)
ios:
	@echo "Building iOS IPA..."
	@which buildozer > /dev/null || (echo "Buildozer not found. Install with: pip3 install buildozer" && exit 1)
	buildozer ios debug
	@echo "IPA built: bin/*.ipa"

# Windows build using PyInstaller
windows:
	@echo "Building Windows executable..."
	@which pyinstaller > /dev/null || (echo "PyInstaller not found. Install with: pip3 install pyinstaller" && exit 1)
	pyinstaller --name="AntennaCalculator" \
		--windowed \
		--onefile \
		--icon=assets/icon.ico \
		main.py
	@echo "Windows executable built: dist/AntennaCalculator.exe"

# Icon generation (Android, iOS, Windows only)
icons:
	@echo "Generating icons for mobile and Windows..."
	python3 create_icons.py

# Install buildozer (for mobile builds)
install-buildozer:
	@echo "Installing Buildozer..."
	pip3 install buildozer
	pip3 install cython

# Install PyInstaller (for Windows builds)
install-pyinstaller:
	@echo "Installing PyInstaller..."
	pip3 install pyinstaller

# Check dependencies
check:
	@echo "Checking dependencies..."
	@python3 -c "import kivy; print(f'Kivy: {kivy.__version__}')" || echo "Kivy not installed"
	@which buildozer > /dev/null && echo "Buildozer: installed" || echo "Buildozer: not installed"
	@which pyinstaller > /dev/null && echo "PyInstaller: installed" || echo "PyInstaller: not installed"

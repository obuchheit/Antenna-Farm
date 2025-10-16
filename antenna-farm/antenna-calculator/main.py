"""
Antenna Calculator - Cross-Platform Kivy Application
Implements DL6WU Yagi and L.B. Cebik Moxon antenna calculations
"""

import math
from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.metrics import dp
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle


class YagiCalculator:
    """DL6WU optimized Yagi-Uda antenna calculator with improved spacing algorithm"""

    def __init__(self):
        self.c = 299792458  # Speed of light in m/s

    def calculate(self, frequency, num_elements, wire_diameter, boom_diameter, boom_relation):
        """
        Calculate Yagi antenna dimensions using DL6WU method

        Args:
            frequency: Operating frequency in MHz
            num_elements: Total number of elements (min 3)
            wire_diameter: Element wire diameter in mm
            boom_diameter: Boom diameter in mm
            boom_relation: "center_connected", "isolated_above", or "insulated_boom"

        Returns:
            Dictionary with element lengths and spacing
        """
        # Convert to meters
        wire_diameter = wire_diameter / 1000
        boom_diameter = boom_diameter / 1000

        # Calculate wavelength
        wavelength = self.c / (frequency * 1e6)

        # DL6WU scaling factors
        director_length_factor = 0.97775
        reflector_length_factor = 1.05

        # Boom correction factor
        boom_correction_factor = 1.0
        if boom_relation == "center_connected":
            boom_correction_factor = 0.98
        elif boom_relation == "isolated_above":
            boom_correction_factor = 0.97

        def length_correction(length):
            """Apply boom and wire diameter corrections"""
            corrected_length = length - (wire_diameter + boom_diameter) * 0.5
            corrected_length *= boom_correction_factor
            return corrected_length

        # Calculate element lengths
        driven_element_length = length_correction(0.5 * wavelength)
        reflector_length = length_correction(reflector_length_factor * driven_element_length)

        director_lengths = []
        for i in range(num_elements - 2):
            dir_length = length_correction(
                director_length_factor * driven_element_length * (1 - i * (0.004 * wavelength))
            )
            director_lengths.append(dir_length)

        # DL6WU optimized spacing factors (non-uniform for better performance)
        spacing_factors = [
            0.075, 0.18, 0.215, 0.25, 0.28, 0.3, 0.315, 0.33,
            0.345, 0.36, 0.375, 0.385, 0.39, 0.395
        ]

        # Calculate spacing
        driven_element_spacing = 0.2 * wavelength
        dir_spacing = []
        space_from_reflector = []
        total = driven_element_spacing

        for i in range(num_elements - 1):
            if i < 14:
                spacing = wavelength * spacing_factors[i]
            else:
                spacing = wavelength * 0.4

            dir_spacing.append(spacing)
            total += spacing
            space_from_reflector.append(total)

        # Total boom length
        boom_length = space_from_reflector[-1] if space_from_reflector else driven_element_spacing

        return {
            'wavelength': wavelength,
            'reflector_length': reflector_length,
            'driven_element_length': driven_element_length,
            'driven_element_spacing': driven_element_spacing,
            'director_lengths': director_lengths,
            'director_spacing': dir_spacing,
            'spacing_from_reflector': space_from_reflector,
            'boom_length': boom_length
        }


class MoxonCalculator:
    """L.B. Cebik polynomial-based Moxon rectangle antenna calculator"""

    def calculate(self, frequency, wire_diameter):
        """
        Calculate Moxon antenna dimensions using Cebik polynomials

        Args:
            frequency: Operating frequency in MHz
            wire_diameter: Wire diameter in mm

        Returns:
            Dictionary with dimensions A, B, C, D in meters and feet, plus any warnings
        """
        # Calculate wavelength in mm
        wavelength = 299792.5 / frequency

        # Normalized diameter
        dw = wire_diameter / wavelength
        d1 = 0.4342945 * math.log(dw)

        # Check valid range
        note = None
        if d1 < -6:
            note = "Wire diameter too small, results uncertain"
        elif d1 > -2:
            note = "Wire diameter too large, results uncertain"

        # Cebik polynomial coefficients
        a = -0.0008571428571 * (d1 * d1) - 0.009571428571 * d1 + 0.3398571429
        b = -0.002142857143 * (d1 * d1) - 0.02035714286 * d1 + 0.008285714286
        c = 0.001809523381 * (d1 * d1) + 0.01780952381 * d1 + 0.05164285714
        d = 0.001 * d1 + 0.07178571429

        # Convert to meters
        a_m = a * wavelength / 1000
        b_m = b * wavelength / 1000
        c_m = c * wavelength / 1000
        d_m = d * wavelength / 1000

        # Convert to feet
        a_ft = a_m * 3.28084
        b_ft = b_m * 3.28084
        c_ft = c_m * 3.28084
        d_ft = d_m * 3.28084

        return {
            'a_m': round(a_m, 4),
            'b_m': round(b_m, 4),
            'c_m': round(c_m, 4),
            'd_m': round(d_m, 4),
            'a_ft': round(a_ft, 4),
            'b_ft': round(b_ft, 4),
            'c_ft': round(c_ft, 4),
            'd_ft': round(d_ft, 4),
            'wavelength': wavelength / 1000,  # in meters
            'note': note
        }


class YagiTab(TabbedPanelItem):
    """Yagi Calculator UI Tab"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text = 'Yagi (DL6WU)'
        self.calculator = YagiCalculator()
        self.build_ui()

    def build_ui(self):
        """Build the Yagi calculator UI"""
        main_layout = BoxLayout(orientation='vertical', padding=dp(10), spacing=dp(10))

        # Input section
        input_grid = GridLayout(cols=2, spacing=dp(10), size_hint_y=None)
        input_grid.bind(minimum_height=input_grid.setter('height'))

        # Frequency
        input_grid.add_widget(Label(text='Frequency:', size_hint_y=None, height=dp(40)))
        freq_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=dp(40))
        self.freq_input = TextInput(text='144.0', multiline=False, input_filter='float')
        self.freq_unit = Spinner(
            text='MHz',
            values=('Hz', 'kHz', 'MHz', 'GHz'),
            size_hint_x=0.3
        )
        freq_layout.add_widget(self.freq_input)
        freq_layout.add_widget(self.freq_unit)
        input_grid.add_widget(freq_layout)

        # Number of elements
        input_grid.add_widget(Label(text='Elements:', size_hint_y=None, height=dp(40)))
        self.elements_input = TextInput(text='5', multiline=False, input_filter='int', size_hint_y=None, height=dp(40))
        input_grid.add_widget(self.elements_input)

        # Wire diameter
        input_grid.add_widget(Label(text='Wire Diameter (mm):', size_hint_y=None, height=dp(40)))
        self.wire_dia_input = TextInput(text='5.0', multiline=False, input_filter='float', size_hint_y=None, height=dp(40))
        input_grid.add_widget(self.wire_dia_input)

        # Boom diameter
        input_grid.add_widget(Label(text='Boom Diameter (mm):', size_hint_y=None, height=dp(40)))
        self.boom_dia_input = TextInput(text='20.0', multiline=False, input_filter='float', size_hint_y=None, height=dp(40))
        input_grid.add_widget(self.boom_dia_input)

        # Boom relation
        input_grid.add_widget(Label(text='Boom Relation:', size_hint_y=None, height=dp(40)))
        self.boom_relation = Spinner(
            text='center_connected',
            values=('center_connected', 'isolated_above', 'insulated_boom'),
            size_hint_y=None,
            height=dp(40)
        )
        input_grid.add_widget(self.boom_relation)

        # Unit selection
        input_grid.add_widget(Label(text='Display Units:', size_hint_y=None, height=dp(40)))
        self.unit_spinner = Spinner(
            text='Metric (m)',
            values=('Metric (m)', 'Imperial (ft)'),
            size_hint_y=None,
            height=dp(40)
        )
        input_grid.add_widget(self.unit_spinner)

        main_layout.add_widget(input_grid)

        # Calculate button
        calc_btn = Button(text='Calculate', size_hint_y=None, height=dp(50))
        calc_btn.bind(on_press=self.calculate)
        main_layout.add_widget(calc_btn)

        # Results section
        scroll = ScrollView(size_hint=(1, 1))
        self.results_label = Label(
            text='Enter values and press Calculate',
            markup=True,
            size_hint_y=None,
            halign='left',
            valign='top'
        )
        self.results_label.bind(texture_size=self.results_label.setter('size'))
        scroll.add_widget(self.results_label)
        main_layout.add_widget(scroll)

        self.add_widget(main_layout)

    def calculate(self, instance):
        """Perform Yagi calculation and display results"""
        try:
            # Get input values
            freq = float(self.freq_input.text)
            unit_multipliers = {'Hz': 1e-6, 'kHz': 1e-3, 'MHz': 1, 'GHz': 1e3}
            freq = freq * unit_multipliers[self.freq_unit.text]

            num_elements = int(self.elements_input.text)
            wire_diameter = float(self.wire_dia_input.text)
            boom_diameter = float(self.boom_dia_input.text)
            boom_relation = self.boom_relation.text

            # Validate inputs
            if freq <= 0:
                raise ValueError("Frequency must be positive")
            if num_elements < 3:
                raise ValueError("Minimum 3 elements required")
            if wire_diameter <= 0 or boom_diameter <= 0:
                raise ValueError("Diameters must be positive")

            # Calculate
            results = self.calculator.calculate(freq, num_elements, wire_diameter, boom_diameter, boom_relation)

            # Format output
            is_metric = self.unit_spinner.text == 'Metric (m)'
            unit = 'm' if is_metric else 'ft'
            conv = 1 if is_metric else 3.28084

            output = f"[b][color=00FF00]DL6WU Yagi Antenna Calculator[/color][/b]\n\n"
            output += f"[b]Frequency:[/b] {freq:.3f} MHz\n"
            output += f"[b]Wavelength:[/b] {results['wavelength'] * conv:.4f} {unit}\n"
            output += f"[b]Elements:[/b] {num_elements}\n"
            output += f"[b]Boom Length:[/b] {results['boom_length'] * conv:.4f} {unit}\n\n"

            output += f"[b][color=FFFF00]Element Dimensions:[/color][/b]\n"
            output += f"[b]Reflector:[/b] {results['reflector_length'] * conv:.4f} {unit}\n"
            output += f"[b]Driven Element:[/b] {results['driven_element_length'] * conv:.4f} {unit}\n"

            for i, length in enumerate(results['director_lengths'], 1):
                output += f"[b]Director {i}:[/b] {length * conv:.4f} {unit}\n"

            output += f"\n[b][color=FFFF00]Spacing from Reflector:[/color][/b]\n"
            output += f"[b]Driven Element:[/b] {results['driven_element_spacing'] * conv:.4f} {unit}\n"

            for i, spacing in enumerate(results['spacing_from_reflector'], 1):
                output += f"[b]Director {i}:[/b] {spacing * conv:.4f} {unit}\n"

            self.results_label.text = output

        except ValueError as e:
            self.results_label.text = f"[color=FF0000][b]Error:[/b] {str(e)}[/color]"
        except Exception as e:
            self.results_label.text = f"[color=FF0000][b]Error:[/b] {str(e)}[/color]"


class MoxonTab(TabbedPanelItem):
    """Moxon Calculator UI Tab"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text = 'Moxon (Cebik)'
        self.calculator = MoxonCalculator()
        self.build_ui()

    def build_ui(self):
        """Build the Moxon calculator UI"""
        main_layout = BoxLayout(orientation='vertical', padding=dp(10), spacing=dp(10))

        # Input section
        input_grid = GridLayout(cols=2, spacing=dp(10), size_hint_y=None)
        input_grid.bind(minimum_height=input_grid.setter('height'))

        # Frequency
        input_grid.add_widget(Label(text='Frequency:', size_hint_y=None, height=dp(40)))
        freq_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=dp(40))
        self.freq_input = TextInput(text='146.0', multiline=False, input_filter='float')
        self.freq_unit = Spinner(
            text='MHz',
            values=('Hz', 'kHz', 'MHz', 'GHz'),
            size_hint_x=0.3
        )
        freq_layout.add_widget(self.freq_input)
        freq_layout.add_widget(self.freq_unit)
        input_grid.add_widget(freq_layout)

        # Wire diameter
        input_grid.add_widget(Label(text='Wire Diameter (mm):', size_hint_y=None, height=dp(40)))
        self.wire_dia_input = TextInput(text='2.05', multiline=False, input_filter='float', size_hint_y=None, height=dp(40))
        input_grid.add_widget(self.wire_dia_input)

        # Unit selection
        input_grid.add_widget(Label(text='Display Units:', size_hint_y=None, height=dp(40)))
        self.unit_spinner = Spinner(
            text='Both',
            values=('Metric (m)', 'Imperial (ft)', 'Both'),
            size_hint_y=None,
            height=dp(40)
        )
        input_grid.add_widget(self.unit_spinner)

        main_layout.add_widget(input_grid)

        # Calculate button
        calc_btn = Button(text='Calculate', size_hint_y=None, height=dp(50))
        calc_btn.bind(on_press=self.calculate)
        main_layout.add_widget(calc_btn)

        # Results section
        scroll = ScrollView(size_hint=(1, 1))
        self.results_label = Label(
            text='Enter values and press Calculate',
            markup=True,
            size_hint_y=None,
            halign='left',
            valign='top'
        )
        self.results_label.bind(texture_size=self.results_label.setter('size'))
        scroll.add_widget(self.results_label)
        main_layout.add_widget(scroll)

        self.add_widget(main_layout)

    def calculate(self, instance):
        """Perform Moxon calculation and display results"""
        try:
            # Get input values
            freq = float(self.freq_input.text)
            unit_multipliers = {'Hz': 1e-6, 'kHz': 1e-3, 'MHz': 1, 'GHz': 1e3}
            freq = freq * unit_multipliers[self.freq_unit.text]

            wire_diameter = float(self.wire_dia_input.text)

            # Validate inputs
            if freq <= 0:
                raise ValueError("Frequency must be positive")
            if wire_diameter <= 0:
                raise ValueError("Wire diameter must be positive")

            # Calculate
            results = self.calculator.calculate(freq, wire_diameter)

            # Format output
            output = f"[b][color=00FF00]Moxon Rectangle Antenna Calculator[/color][/b]\n"
            output += f"[b]L.B. Cebik Polynomial Method[/b]\n\n"
            output += f"[b]Frequency:[/b] {freq:.3f} MHz\n"
            output += f"[b]Wavelength:[/b] {results['wavelength']:.4f} m\n"
            output += f"[b]Wire Diameter:[/b] {wire_diameter:.2f} mm\n\n"

            if results['note']:
                output += f"[color=FF6600][b]Warning:[/b] {results['note']}[/color]\n\n"

            output += f"[b][color=FFFF00]Dimensions:[/color][/b]\n\n"

            unit_choice = self.unit_spinner.text

            if unit_choice in ('Metric (m)', 'Both'):
                output += "[b]Metric (meters):[/b]\n"
                output += f"  A (Element half-length): {results['a_m']:.4f} m\n"
                output += f"  B (Tail length): {results['b_m']:.4f} m\n"
                output += f"  C (Tail spacing): {results['c_m']:.4f} m\n"
                output += f"  D (Element spacing): {results['d_m']:.4f} m\n\n"

            if unit_choice in ('Imperial (ft)', 'Both'):
                output += "[b]Imperial (feet):[/b]\n"
                output += f"  A (Element half-length): {results['a_ft']:.4f} ft\n"
                output += f"  B (Tail length): {results['b_ft']:.4f} ft\n"
                output += f"  C (Tail spacing): {results['c_ft']:.4f} ft\n"
                output += f"  D (Element spacing): {results['d_ft']:.4f} ft\n\n"

            output += "[b][color=CCCCCC]Dimension Reference:[/color][/b]\n"
            output += "A: Half-length of each element\n"
            output += "B: Length of tail section\n"
            output += "C: Spacing between tail ends\n"
            output += "D: Spacing between driven and reflector\n"

            self.results_label.text = output

        except ValueError as e:
            self.results_label.text = f"[color=FF0000][b]Error:[/b] {str(e)}[/color]"
        except Exception as e:
            self.results_label.text = f"[color=FF0000][b]Error:[/b] {str(e)}[/color]"


class AboutTab(TabbedPanelItem):
    """About information tab"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text = 'About'
        self.build_ui()

    def build_ui(self):
        """Build the About tab UI"""
        scroll = ScrollView()
        about_text = Label(
            text="""[b][color=00FF00]Antenna Calculator[/color][/b]
[b]Version 1.0[/b]

Cross-platform antenna design calculator for amateur radio.

[b][color=FFFF00]Features:[/color][/b]

[b]Yagi-Uda (DL6WU Method):[/b]
• Optimized spacing algorithm
• Variable element count (3+)
• Boom correction factors
• Supports multiple mounting methods

[b]Moxon Rectangle (L.B. Cebik):[/b]
• Polynomial-based calculations
• High accuracy within design range
• Compact directional antenna
• Easy to build

[b][color=FFFF00]Calculation Methods:[/color][/b]

[b]DL6WU Yagi:[/b]
Based on the DL6WU long Yagi design method with
optimized element spacing for maximum gain and
front-to-back ratio. Uses non-uniform spacing
with correction factors for boom and wire diameter.

[b]L.B. Cebik Moxon:[/b]
Implements L.B. Cebik's polynomial equations for
Moxon rectangle antennas. Provides high-precision
dimensions for wire diameters in the valid range.

[b][color=FFFF00]Platform Support:[/color][/b]
• Android
• iOS
• Windows
• macOS
• Linux

[b]Developer:[/b] Ham Radio Tools
[b]License:[/b] Open Source

For source code and updates:
https://github.com/antenna-calculator

73!""",
            markup=True,
            size_hint_y=None,
            halign='left',
            valign='top'
        )
        about_text.bind(texture_size=about_text.setter('size'))
        scroll.add_widget(about_text)
        self.add_widget(scroll)


class AntennaCalculatorApp(App):
    """Main application class"""

    def build(self):
        """Build the application UI"""
        # Set window background
        Window.clearcolor = (0.1, 0.1, 0.15, 1)

        # Create tabbed panel
        tab_panel = TabbedPanel(do_default_tab=False, tab_width=dp(150))

        # Add tabs
        tab_panel.add_widget(YagiTab())
        tab_panel.add_widget(MoxonTab())
        tab_panel.add_widget(AboutTab())

        return tab_panel


if __name__ == '__main__':
    AntennaCalculatorApp().run()

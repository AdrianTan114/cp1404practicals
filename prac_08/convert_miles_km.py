"""Convert miles to km in GUI-based program."""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM_RATE = 1.60934


class ConvertDistanceApp(App):
    """Interface-driven program that converts user-entered miles to kilometres."""
    message = StringProperty()

    def build(self):
        """Build the Kivy app from kv file."""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file("convert_miles_km.kv")
        return self.root

    def handle_convert(self):
        """Handle conversion, output result to label."""
        miles = self.get_valid_miles()
        km = miles * MILES_TO_KM_RATE
        self.message = str(km)

    def handle_increment(self, change):
        """Handle incrementing input text."""
        value = self.get_valid_miles() + change
        self.root.ids.input_number.text = str(value)
        self.handle_convert()

    def get_valid_miles(self):
        """Error check miles to ensure it is a float."""
        try:
            miles = float(self.root.ids.input_number.text)
            return miles
        except ValueError:
            return 0.0


ConvertDistanceApp().run()

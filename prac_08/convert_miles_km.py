"""Convert miles to km in GUI-based program."""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty


class ConvertDistanceApp(App):
    """Interface-driven program that converts user-entered miles to kilometres."""
    message = StringProperty()

    def build(self):
        """Build the Kivy app from kv file."""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file("convert_miles_km.kv")
        return self.root

    def handle_convert(self, miles):
        """Handle conversion, output result to label."""
        km = float(miles) * 1.60934
        self.message = str(km)

    def handle_increment(self, change):
        """Handle incrementing input text."""
        value = float(self.root.ids.input_number.text) + change
        self.root.ids.input_number.text = str(value)


ConvertDistanceApp().run()

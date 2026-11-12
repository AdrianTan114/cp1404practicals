"""Prac 08 Dynamical Labels exercise."""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ["Steve", "Tony", "Bruce", "Clint", "Natasha", "Thor"]

    def build(self):
        self.title = "Dynamic Names"
        self.root = Builder.load_file("dynamic_labels.kv")
        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.main.add_widget(temp_label)
        return self.root


DynamicLabelsApp().run()

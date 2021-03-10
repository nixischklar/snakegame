from kivy.uix.widget import Widget
from kivy.uix.colorpicker import ColorPicker


class Color(Widget):
    def __init__(self):
        super().__init__()

        color_picker = ColorPicker()
        self.add_widget(color_picker)
        color_picker.bind(color=self.on_color)

    def on_color(instance, value):
        print("RGBA = ", str(value))
        print("HSV = ", str(instance.hsv))
        print("HEX = ", str(instance.hex_color))


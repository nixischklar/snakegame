from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label


class Color(Widget):
    def __init__(self):
        super().__init__()
        self.cols = 2
        self.row = 4
        # Buttons for changing color
        # Color Blue
        self.blue = Button(background_color=blue)
        self.blue.bind(on_press=self.blue_button)
        self.add_widget(self.blue)
        # Color Green
        self.green = Button(background_color=green)
        self.green.bind(on_press=self.green_button)
        self.add_widget(self.green)
        # Color Red
        self.red = Button(background_color=red)
        self.red.bind(on_press=self.red_button)
        self.add_widget(self.red)
        # Color Purple
        self.purple = Button(background_color=purple)
        self.purple.bind(on_press=self.purple_button)
        self.add_widget(self.purple)
        snake_color = Snake()

    def blue_button(self):
        self.snake_color = blue
        self.add_widget(Label(text='You changed the color!'))

    def green_button(self):
        for i in self.snake_color:
            self.body = green
            continue

    def red_button(self):
        for i in self.snake_color:
            self.body = red

    def purple_button(self):
        for i in self.snake_color:
            self.body = purple
            continue


from random import randint
import kivy
from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.properties import ObjectProperty, NumericProperty, StringProperty
from kivy.uix.colorpicker import ColorPicker
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
import cProfile
from kivy.uix.widget import Widget
from kivy.vector import Vector
from snake import Snake
from kivy.config import Config
from snake import SnakeApp
from kivy.lang.builder import Builder

red = [1, 0, 0, 1]
green = [0, 1, 0, 1]
blue = [0, 0, 1, 1]
purple = [1, 0, 1, 1]


class StartPage(GridLayout):
    def __init__(self, **kwargs):
        super(StartPage, self).__init__(**kwargs)

    def connect_button(self, instance):
        snake_game.screen_manager.current = "Connect"
        self.add_widget(Label(text='', font_size=30))


class ClosePage(GridLayout):
    def __init__(self, **kwargs):
        super(ClosePage, self).__init__(**kwargs)


class RulePage(GridLayout):
    def __init__(self, **kwargs):
        super(RulePage, self).__init__(**kwargs)
        self.rows = 1
        self.cols = 2
        self.add_widget(Label(text='Spielregeln:'))
        self.connect = Button(text="Main Menu")
        self.connect.bind(on_press=self.connect_button)
        self.add_widget(self.connect)

    def connect_button(self, instance):
        snake_game.screen_manager.current = "Connect"
        self.add_widget(Label(text='', font_size=30))


class ColorPage(GridLayout):
    def __init__(self, **kwargs):
        super(ColorPage, self).__init__(**kwargs)
        self.cols = 2
        self.row = 2
        # Buttons for changing color
        # Color Blue
        self.lime = Button(background_color=blue)
        self.lime.bind(on_press=self.blue_button)
        self.add_widget(self.lime)
        # Color Green
        self.green = Button(background_color=green)
        self.green.bind(on_press=self.green_button)
        self.add_widget(self.green)
        # Color Red
        self.red = Button(background_color=red)
        self.red.bind(on_press=self.red_button)
        self.add_widget(self.red)
        # Color Purple
        self.blue = Button(background_color=purple)
        self.blue.bind(on_press=self.purple_button)
        self.add_widget(self.blue)

    def blue_button(self):
        for i in self.body:
            self.body = blue
            continue

    def green_button(self):
        for i in self.body:
            self.body = green
            continue

    def red_button(self):
        for i in self.body:
            self.body = red

    def purple_button(self):
        for i in self.body:
            self.body = purple
            continue


class ConnectPage(GridLayout):
    def __init__(self, **kwargs):
        super(ConnectPage, self).__init__(**kwargs)
        self.rows = 2
        self.cols = 2
        self.start = Button(text="Start")
        self.start.bind(on_press=self.on_start)
        self.add_widget(self.start)

        self.close = Button(text="Close")
        self.close.bind(on_press=self.on_stop)
        self.add_widget (self.close)

        self.rule = Button(text="Rules")
        self.rule.bind(on_press=self.rule_button)
        self.add_widget(self.rule)

        self.color = Button(text="Change Color")
        self.color.bind(on_press=self.color_button)
        self.add_widget(self.color)

    def rule_button(self, instance):
        snake_game.screen_manager.current = "Rule"

    def color_button(self, instance):
        snake_game.screen_manager.current = "Color"

    def on_stop(self, instance):
        self.profile.disable()
        self.profile.dump_stats('snake_game.profile')

    def on_start(self, instance):
        snake_game.screen_manager.current = "Start"
        snake = Snake()
        Snake.restart_game(snake)


class SnakeGame(App):
    def build(self):
        self.screen_manager = ScreenManager()

        self.connect_page = ConnectPage()
        screen = Screen(name="Connect")
        screen.add_widget(self.connect_page)
        self.screen_manager.add_widget(screen)

        self.start_page = StartPage()
        screen = Screen(name="Start")
        screen.add_widget(self.start_page)
        self.screen_manager.add_widget(screen)

        self.close_page = ClosePage()
        screen = Screen(name="Close")
        screen.add_widget(self.close_page)
        self.screen_manager.add_widget(screen)

        self.rule_page = RulePage()
        screen = Screen(name="Rule")
        screen.add_widget(self.rule_page)
        self.screen_manager.add_widget(screen)

        self.color_page = ColorPage()
        screen = Screen(name="Color")
        screen.add_widget(self.color_page)
        self.screen_manager.add_widget(screen)

        return self.screen_manager


if __name__ == "__main__":
    snake_game = SnakeGame()
    snake_game.run()



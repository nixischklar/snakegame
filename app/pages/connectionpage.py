from snakegame.other import color
from snakegame.other.color import Color
from app import main
from app.main import snake_game
from snakegame import main
from snakegame.main import SnakeApp
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button


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
        self.add_widget(self.close)

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
        chose_color = Color()
        chose_color.run()

    def on_stop(self, instance):
        self.profile.disable()
        self.profile.dump_stats('snake_game.profile')

    def on_start(self, instance):
        snake_game.screen_manager.current = "Start"
        snake_app = SnakeApp()
        snake_app.run()

from app import main
from app.main import snake_game
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class StartPage(GridLayout):
    def __init__(self, **kwargs):
        super(StartPage, self).__init__(**kwargs)
        self.cols = 1
        self.rows = 2

        self.connect = Button(text="Main Menu")
        self.connect.bind(on_press=self.connect_button)
        self.add_widget(self.connect)

    def connect_button(self, instance):
        snake_game.screen_manager.current = "Connect"
        self.add_widget(Label(text='', font_size=30))

from app.pages.closepage import ClosePage
from kivy.uix.screenmanager import ScreenManager
from kivy.app import App
from kivy.uix.screenmanager import Screen
from app.pages.colorpage import ColorPage
from app.pages.moduspage import ModusPage
from app.pages.scorepage import ScorePage
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button


class ConnectPage(GridLayout):
    def __init__(self, **kwargs):
        super(ConnectPage, self).__init__(**kwargs)
        self.rows = 2
        self.cols = 2

        self.modus = Button(text="Modus")
        self.modus.bind(on_press=self.modus_button)
        self.add_widget(self.modus)

        self.close = Button(text="Close")
        self.close.bind(on_press=self.on_stop)
        self.add_widget(self.close)

        self.score = Button(text="Score")
        self.score.bind(on_press=self.score_button)
        self.add_widget(self.score)

        self.color = Button(text="Color")
        self.color.bind(on_press=self.color_button)
        self.add_widget(self.color)

    def score_button(self, instance):
        snake_game.screen_manager.current = "Score"

    def color_button(self, instance):
        snake_game.screen_manager.current = "Color"

    def on_stop(self, instance):
        self.profile.disable()
        self.profile.dump_stats('snake_game.profile')

    def modus_button(self, instance):
        snake_game.screen_manager.current = "Modus"


class SnakeGame(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.color_page = ColorPage()
        self.score_page = ScorePage()
        self.close_page = ClosePage()
        self.modus_page = ModusPage()
        self.connect_page = ConnectPage()
        self.screen_manager = ScreenManager()

    def build(self):
        screen = Screen(name="Connect")
        screen.add_widget(self.connect_page)
        self.screen_manager.add_widget(screen)

        screen = Screen(name="Modus")
        screen.add_widget(self.modus_page)
        self.screen_manager.add_widget(screen)

        screen = Screen(name="Close")
        screen.add_widget(self.close_page)
        self.screen_manager.add_widget(screen)

        screen = Screen(name="Score")
        screen.add_widget(self.score_page)
        self.screen_manager.add_widget(screen)

        screen = Screen(name="Color")
        screen.add_widget(self.color_page)
        self.screen_manager.add_widget(screen)

        return self.screen_manager


if __name__ == "__main__":
    snake_game = SnakeGame()
    snake_game.run()

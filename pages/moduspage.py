from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from app.multiplayer.multiplayer import Multiplayer
from app.pages.multiplayerpage import MultiPlayerPage
from app.pages.startpage import StartPage
from app.snake.mainsnake import SnakeApp


class ModusPage(Screen):
    def __init__(self, **kwargs):
        super(ModusPage, self).__init__(**kwargs)
        self.cols = 1
        self.rows = 2

        self.start = Button(text="Start")
        self.start.bind(on_press=self.on_start)
        self.add_widget(self.start)

        self.multiplayer = Button(text="Multiplayer")
        self.multiplayer.bind(on_press=self.multi_player)
        self.add_widget(self.multiplayer)

    def on_start(self, instance):
        mm.screen_manager.current = "Start"
        snake_app = SnakeApp()
        snake_app.run()

    def multi_player(self, instance):
        mm.screen_manager.current = "Multiplayer"
        multiplayer_app = Multiplayer()
        multiplayer_app.run()


class ModusScreenManager(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.start_page = StartPage()
        self.multiplayer_page = MultiPlayerPage()
        self.screen_manager = ScreenManager()
        self.modus_page = ModusPage()

    def build(self):
        screen = Screen(name="Start")
        screen.add_widget(self.start_page)
        self.screen_manager.add_widget(screen)

        screen = Screen(name="Multiplayer")
        screen.add_widget(self.multiplayer_page)
        self.screen_manager.add_widget(screen)

        screen = Screen(name="Modus")
        screen.add_widget(self.modus_page)
        self.screen_manager.add_widget(screen)

        return self.screen_manager


if __name__ == "__main__":
    mm = ModusScreenManager()
    mm.run()

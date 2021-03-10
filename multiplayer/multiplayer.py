from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window


class Game(Widget):
    def __init__(self, **kwargs):
        super(Game, self).__init__(**kwargs)
        self._keyboard = Window.requst


class Multiplayer(App):
    def build(self):
        pass


if __name__ == '__main__':
    Multiplayer().run()

from snakegame import mainsnake
from snakegame.mainsnake import Snake
from kivy.app import App

Window_Height = 700
Window_Width = 800

red = [1, 0, 0, 1]
green = [0, 1, 0, 1]
blue = [0, 0, 1, 1]
purple = [1, 0, 1, 1]

Player_Size = 40
Game_Speed = .1


class SnakeApp(App):
    def build(self):
        game = Snake()
        return game


if __name__ == '__main__':
    SnakeApp().run()

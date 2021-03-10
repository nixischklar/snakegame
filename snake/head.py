from kivy.uix.widget import Widget
from kivy.vector import Vector


Player_Size = 40


class SnakeHead(Widget):
    orientation = (Player_Size, 0)

    def reset_pos(self):
        self.pos = (0, 0)
        self.orientation = (Player_Size, 0)

    def move(self):
        self.pos = Vector(*self.orientation) + self.pos


from kivy.app import App
from app.other.food import Faster
from app.other.food import Slower
from app.other.food import Smaller
from app.other.food import Bigger
from app.other.grid import SmartGrid
from app.snake.head import SnakeHead
from app.snake.body import SnakeBody
from kivy.uix.widget import Widget
from kivy.properties import StringProperty
from kivy.core.window import Window
from kivy.clock import Clock
from random import randint


Window_Height = 700
Window_Width = 800

red = [1, 0, 0, 1]
green = [0, 1, 0, 1]
blue = [0, 0, 1, 1]
purple = [1, 0, 1, 1]

Player_Size = 40
Game_Speed = .1


class Snake(Widget):
    head = SnakeHead()
    body = SnakeBody()
    bigger = Bigger()
    smaller = Smaller()
    faster = Faster()
    slower = Slower()
    player_size = Player_Size
    game_over = StringProperty("")

    def __init__(self):
        super(Snake, self).__init__()
        Window.size = (Window_Width, Window_Height)
        Window.bind(on_key_down=self.key_action)
        self.pos = (0, 0)
        self.timer = Clock.schedule_interval(self.refresh, Game_Speed)
        self.body = []
        self.restart_game()

    def restart_game(self):
        self.occupied = SmartGrid()
        self.timer.cancel()
        self.timer = Clock.schedule_interval(self.refresh, Game_Speed)
        self.head.reset_pos()
        self.score = 0

        for block in self.body:
            self.remove_widget(block)

        self.body = []

        self.body.append(
            SnakeBody(
                pos=(self.head.pos[0] - Player_Size, self.head.pos[1]),
                size=self.head.size
            )
        )
        self.add_widget(self.body[-1])
        self.occupied[self.body[-1].pos] = True

        self.body.append(
            SnakeBody(
                pos=(self.head.pos[0] - 2 * Player_Size, self.head.pos[1]),
                size=self.head.size
            )
        )

        self.add_widget(self.body[-1])
        self.occupied[self.body[1].pos] = True
        self.spawn_bigger()

    def refresh(self, dt):
        if not (0 <= self.head.pos[0] < Window_Width) or \
                not (0 <= self.head.pos[1] < Window_Height):

            self.restart_game()
            return

        if self.occupied[self.head.pos] is True:
            self.restart_game()
            return

        self.occupied[self.body[-1].pos] = False
        self.body[-1].move(self.body[-2].pos)

        for i in range(2, len(self.body)):
            self.body[-i].move(new_pos=self.body[-(i + 1)].pos)

        self.body[0].move(new_pos=self.head.pos)
        self.occupied[self.body[0].pos] = True

        self.head.move()

        if self.head.pos == self.bigger.pos:
            self.score += 10
            self.body.append(
                SnakeBody(
                    pos=self.head.pos,
                    size=self.head.size
                )
            )
            self.add_widget((self.body[-1]))
            self.spawn.bigger()

    def spawn_bigger(self):
        roll = self.pos
        found = False
        while not found:
            roll = [Player_Size *
                    randint(0, int(Window_Width / Player_Size) - 1),
                    Player_Size *
                    randint(0, int(Window_Height / Player_Size) - 1)]
            if self.occupied[roll] is True or \
                    roll == self.head.pos:
                continue

            found = True
        self.bigger.move(roll)

    def key_action(self, *args):
        command = list(args)[3]
        if command == "w" or command == 'up':
            self.head.orientation = (0, Player_Size)
        elif command == "s" or command == 'down':
            self.head.orientation = (0, -Player_Size)
        elif command == "a" or command == 'left':
            self.head.orientation = (-Player_Size, 0)
        elif command == "d" or command == 'right':
            self.head.orientation = (Player_Size, 0)
        elif command == 'r':
            self.restart_game()


class SnakeApp(App):
    def build(self):
        game = Snake()
        return game


if __name__ == '__main__':
    SnakeApp().run()

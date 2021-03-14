import os
import time
import clock
import random
import gc
import keyboard
import threading
import json
import pygame as pg

blue = (25, 68, 133)
red = (201, 12, 53)
yellow = (255, 238, 3)
green = (12, 148, 23)
violet = (75, 1, 140)
pink = (255, 82, 235)
black = (0, 0, 0)


# Init
# delay = 0.1
# score = 0
# high_score = 0


# WN2 (Game)
#     wn = pygame
#     wn.title("Snake Game with Plot Twist")
#     wn.setup(width=800, height=800)
#     wn.tracer(0)
#     wn.bgcolor("white")
#     # Snake Head
#     head = turtle.Turtle()
#     head.speed(0)
#     head.shape("square")
#     head.color("black")
# head.penup()
# head.goto(0, 0)
# head.direction = "stop"
# Food
# slow_food = turtle.Turtle()
# slow_food.speed(0)
# slow_food.color("purple")
# slow_food.penup()
# slow_food.goto(0, 100)
# slow_food.shape("square")
# x = random.randint(-290, 290)
# y = random.randint(-290, 290)

# class Images:   only if this bs comes gööd
# def __init__(self):
# self.name = "images"
# self.append_apple = "🍌"
# self.

class Score:
    def draw_score(self, surface):
        score, high_score = (0, 0)
        name = pg.font.match_font('arial')
        if score > high_score:
            high_score = score
        font = pg.font.Font(name, 18)
        text_surface = font.render('Score: {} High Score: {}'.format(score, high_score), True, yellow)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (390, 10)
        surface.blit(text_surface, text_rect)


class Canvas:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        wn = pg.display.set_mode((height, width))
        pg.display.set_caption('Classic Snake Game')


class Segments:
    def __init__(self):
        self.segments = []


class Body:
    def __init__(self, width, height):
        self.body = []
        self.body_color = 'black'  # color implement (classes)
        self.body_rect.x = width / 2
        self.body_rect.y = height / 4
        self.width = 10
        self.height = 10

    def draw_body(self, surface):
        self.body_rect = pg.Rect(self.body_rect.x, self.body_rect.y, self.width, self.height)
        pg.draw.rect(surface, self.body_color, self.body_rect)

    def add_unit(self):
        if len(self.body) != 0:
            index = len(self.body) - 1
            x = self.body[index][0]
            y = self.body[index][1]
            self.body.append([x, y])
        else:
            self.body.append([1000, 1000])


class Head:
    def __init__(self, width, height, body, body_color, segments):
        self.head_rect.x = width / 2
        self.head_rect.y = height / 4
        self.width = 10
        self.height = 10
        self.body_color = body_color
        self.body = body
        self.segments = segments
        self.head_rect.velocity = 10
        self.head_rect.dir = 'stop'
        self.color = 'black'  # color implement (classes)

    def draw_head(self, surface):
        self.head_rect = pg.Rect(self.head_rect.x, self.head_rect.y, self.width, self.height)
        pg.draw.rect(surface, self.color, self.head_rect)
        if len(self.body) > 0:
            for unit in self.body:
                segment = pg.Rect(unit[0], unit[1], self.width, self.height)
                pg.draw.rect(surface, self.body_color, segment)

    def collision(self):
        for segment in self.segments:
            if self.head_rect.colliderect(segment):
                return True
        if self.head_rect.y < 0 or self.head_rect.y > height - self.height or self.head_rect.x < 0 or self.head_rect.x > width - self.width:
            return True

    def random_pos(self):
        self.head_rect.x = 0
        self.head_rect.y = 0


class Apple:
    def __init__(self, width, height):
        self.apple_rect.x = width / 2
        self.apple_rect.y = height / 4
        self.width = 10
        self.height = 10
        self.color = red

    def draw_apple(self, surface):
        self.apple_rect = pg.Rect(self.apple_rect.x, self.apple_rect.y, self.width, self.height)
        pg.draw.rect(surface, self.color, self.apple_rect)

    def random_pos(self, width, height):
        self.apple_rect.x = random.randint(0, width - self.width)
        self.apple_rect.y = random.randint(0, height - self.height)

    def eaten(self):
        return self.apple_rect.colliderect(head)


# class Banana:
#     def __init__(self, width, height):
#         self.banana_rect.x = width / 2
#         self.banana_rect.y = height / 4
#         self.width = 10
#         self.height = 10
#         self.color = yellow
#
#     def draw_banana(self, surface):
#         self.banana_rect = pg.Rect(self.banana_rect.x, self.banana_rect.y, self.width, self.height)
#         pg.draw.rect(surface, self.color, self.banana_rect)
#
#     def random_pos(self, width, height):
#         self.banana_rect.x = random.randint(0, width - self.width)
#         self.banana_rect.y = random.randint(0, height - self.height)
#
#     def eaten(self):
#         return self.banana_rect.colliderect(head)
#
#
# class Peach:
#     def __init__(self, width, height):
#         self.peach_rect.x = width / 2
#         self.peach_rect.y = height / 4
#         self.width = 10
#         self.height = 10
#         self.color = yellow
#
#     def draw_peach(self, surface):
#         self.peach_rect = pg.Rect(self.peach_rect.x, self.peach_rect.y, self.width, self.height)
#         pg.draw.rect(surface, self.color, self.peach_rect)
#
#     def random_pos(self, width, height):
#         self.peach_rect.x = random.randint(0, width - self.width)
#         self.peach_rect.y = random.randint(0, height - self.height)
#
#     def eaten(self):
#         return self.peach_rect.colliderect(head)
#
#
# class Lemon:
#     def __init__(self, width, height):
#         self.lemon_rect.x = width / 2
#         self.lemon_rect.y = height / 4
#         self.width = 10
#         self.height = 10
#         self.color = yellow
#
#     def draw_lemon(self, surface):
#         self.lemon_rect = pg.Rect(self.lemon_rect.x, self.lemon_rect.y, self.width, self.height)
#         pg.draw.rect(surface, self.color, self.lemon_rect)
#
#     def random_pos(self, width, height):
#         self.lemon_rect.x = random.randint(0, width - self.width)
#         self.lemon_rect.y = random.randint(0, height - self.height)
#
#     def eaten(self):
#         return self.lemon_rect.colliderect(head)
#
#
# class Grapes:
#     def __init__(self, width, height):
#         self.grapes_rect.x = width / 2
#         self.grapes_rect.y = height / 4
#         self.width = 10
#         self.height = 10
#         self.color = yellow
#
#     def draw_grapes(self, surface):
#         self.grapes_rect = pg.Rect(self.grapes_rect.x, self.grapes_rect.y, self.width, self.height)
#         pg.draw.rect(surface, self.color, self.grapes_rect)
#
#     def random_pos(self, width, height):
#         self.grapes_rect.x = random.randint(0, width - self.width)
#         self.grapes_rect.y = random.randint(0, height - self.height)
#
#     def eaten(self):
#         return self.grapes_rect.colliderect(head)
#
#
# class Watermelon:
#     def __init__(self, width, height):
#         self.melon_rect.x = width / 2
#         self.melon_rect.y = height / 4
#         self.width = 10
#         self.height = 10
#         self.color = yellow
#
#     def draw_melon(self, surface):
#         self.melon_rect = pg.Rect(self.melon_rect.x, self.melon_rect.y, self.width, self.height)
#         pg.draw.rect(surface, self.color, self.melon_rect)
#
#     def random_pos(self, width, height):
#         self.melon_rect.x = random.randint(0, width - self.width)
#         self.melon_rect.y = random.randint(0, height - self.height)
#
#     def eaten(self):
#         return self.melon_rect.colliderect(head)

# Snake segments (length body)
# class Segment:
#     pen = turtle.Turtle()
#     pen.speed(0)
#     pen.shape("square")
#     pen.color("blue")
#     pen.hideturtle()
#     pen.penup()
#     pen.write("Score : {} High Score : {}".format(score, high_score), align="center", font=("comic sans", 24, "normal"))
#     pen.goto(0, 260)


# Movement & Rules
class Keyboard:
    def __init__(self, body, head_rect):
        self.body = body
        self.head_rect = head_rect

    def directions(self):
        if self.head_rect.dir == 'down' and self.head_rect.dir == 'up':
            self.head_rect.dir = 'up'
        if self.head_rect.dir != 'up' and self.head_rect.dir == 'down':
            self.head_rect.dir = 'down'
        if self.head_rect.dir != 'right' and self.head_rect.dir == 'left':
            self.head_rect.dir = 'left'
        if self.head_rect.dir != 'left' and self.head_rect.dir == 'right':
            self.head_rect.dir = 'right'

    def move(self):
        for index in range(len(self.body) - 1, 0, -1):
            x = self.body[index - 1][0]
            y = self.body[index - 1][1]
            self.body[index] = [x, y]

        if len(self.body) > 0:
            self.body[0] = [self.head_rect.x, self.head_rect.y]

        if self.head_rect.dir == "up":
            self.head_rect.y -= self.head_rect.velocity

        if self.head_rect.dir == "down":
            self.head_rect.y += self.head_rect.velocity

        if self.head_rect.dir == "left":
            self.head_rect.x -= self.head_rect.velocity

        if self.head_rect.dir == "right":
            self.head_rect.x += self.head_rect.velocity


# Movement listen event
class Game:
    def __init__(self, wn, score, direction):
        self.wn = wn
        self.score = score
        self.direction = direction

    def game_over(self):
        game_over_font = pg.font.Font('arial', 24)
        game_over_surf = game_over_font.render('Game Over', True, yellow)
        game_over_rect = game_over_surf.get_rect()
        game_over_rect.midtop = (290, 20)
        self.wn.blit(game_over_surf, game_over_rect)
        score = 0
        pg.display.flip()
        time.sleep(2)           #muss man vielleicht noch rausnehmen wegen endscreen
        run = True              #button erstellen zum nochmal spielen und das rausnehmen
        apple = Apple()
        h = Head()
        b = Body()
        self.start_game(apple, h, b)

    def start_game(self, apple, h, b):
        run = True
        while run:
            clock.tick(30)      #recherchieren was tick() ist
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    run = False
            self.wn.fill(black)
            apple.draw_apple(self.wn)
            h.draw_head(self.wn)
            b.draw_body(self.wn)
            draw.score(self.wn) #schauen wie man das am besten macht mit score

            pressed = pg.key.get_pressed()
            if pressed[pg.K_UP]:
                h.direction('up')
                b.direction('up')
            if pressed[pg.K_DOWN]:
                h.direction('down')
                b.direction('down')
            if pressed[pg.K_LEFT]:
                h.direction('left')
                b.direction('left')
            if pressed[pg.K_RIGHT]:
                h.direction('right')
                b.direction('right')
            h.move()
            b.move()
            if apple.eaten(h.head_rect):
                apple.random_pos()
                b.add_unit()
                self.score += 10
            if h.collision():
                run = False
                self.game_over()

            pg.display.update()



# while True:
#     wn.update()
#     if head.xcor() > 397 or head.xcor() < -397 or head.ycor() > 397 or head.ycor() < -397:
#         time.sleep(0)
#         head.goto(0, 0)
#         head.direction = "stop"
#
#         for segment in segments:
#             segment.goto(1000, 1000)
#         segments.clear()
#
#         score = 0
#         delay = 0.1
#         pen.clear()
#         pen.write("Score : {} High Score : {}".format(score, high_score), align="center",
#                   font=("comic sans", 24, "normal"))
#
#     if head.distance(slow_food) < 20:
#         x = random.randint(-290, 290)
#         y = random.randint(-290, 290)
#         slow_food.goto(x, y)
#         new_segment = turtle.Turtle()
#         new_segment.speed(0)
#         new_segment.shape("square")
#         new_segment.penup()
#         new_segment.goto(0, 0)
#         new_segment.color("red")
#         segments.append(new_segment)
#
#         score += 10
#         if score > high_score:
#             high_score = score
#         pen.clear()
#         pen.write("Score : {} High Score : {}".format(score, high_score),
#                   align="center", font=("comic sans", 24, "normal"))
#         for item in range(len(segments) - 1, 0, -1):
#             x = segments[item - 1].xcor()
#             y = segments[item - 1].ycor()
#             segments[item].goto(x, y)
#         if len(segments) > 0:
#             x = head.xcor()
#             y = head.ycor()
#             segments[0].goto(x, y)
#     move()
#
#     for segment in segments:
#         if segment.distance(head) < 10:
#             time.sleep(1)
#             head.goto(0, 0)
#             head.direction = "stop"
#             for segment in segments:
#                 segment.goto(1000, 1000)
#             segment.clear()
#             score = 0
#             delay = 0.1
#             pen.clear()
#             pen.write("Score : {} High Score : {}".format(score, high_score),
#                       align="center", font=("comic sans", 24, "normal"))
#     time.sleep(delay)
# wn.mainloop()
#
# import kivy
# from kivy.app import App
# from kivy.uix.label import Label
# from kivy.uix.gridlayout import GridLayout
# from kivy.uix.textinput import TextInput
# from kivy.uix.button import Button
# from kivy.uix.screenmanager import ScreenManager, Screen
# import os
#
#
# class ConnectPage(GridLayout):
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         self.cols = 4
#
#         self.start = Button(text="Spiel starten")
#         self.add_widget(self.start)
#
#         self.exit = Button(text="Spiel beenden")
#         self.add_widget(self.exit)
#
#         self.rule = Button(text="Spielregeln")
#         self.add_widget(self.rule)
#
#         self.color = Button(text="Farbe ändern")
#         self.add_widget(self.color)
#
#
# class SnakeApp(App):
#     def build(self):
#         return ConnectPage()
#
#
# if __name__ == "__main__":
#     snake_game = SnakeApp()
#     SnakeApp().run()
#
# Builder.load_string('''
# <Bigger>:
#     canvas:
#         Color:
#             rgb: (1,0,0)
#         Rectangle:
#             pos: self.pos
#             size: self.size
#
# <SnakeHead>:
#     canvas:
#         Color:
#             rgb: (1,1,1)
#         Rectangle:
#             pos: self.pos
#             size: self.size
#
# <SnakeBody>:
#     canvas:
#         Color:
#             rgb: (1,1,1,.8)
#         Rectangle:
#             pos: self.pos
#             size: self.size
#
# <SnakeApp>
#     head: snake_head
#     bigger: snake_bigger
#
#     SnakeHead:
#         id: snake_head
#         size: root.player_size - 2,root.player_size -2
#     Label:
#         size: root.player_size, root.player_size
#         pos: root.size[0] / 10, 9 * root.size[1] / 10
#         text: str(root.score)
#
# ''')

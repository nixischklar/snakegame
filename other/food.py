from kivy.uix.widget import Widget


class Bigger(Widget):
    def move(self, new_pos):
        self.pos = new_pos


class Smaller(Widget):
    def move(self, new_pos):
        self.pos = new_pos


class Faster(Widget):
    def move(self, new_pos):
        self.pos = new_pos


class Slower(Widget):
    def move(self, new_pos):
        self.pos = new_pos


from kivy.uix.screenmanager import Screen


class ScorePage(Screen):
    def __init__(self, **kwargs):
        super(ScorePage, self).__init__(**kwargs)

        self.rows = 1
        self.cols = 2

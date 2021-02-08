from app.pages import closepage
from app.pages.closepage import ClosePage
from app.pages import colorpage
from app.pages.colorpage import ColorPage
from app.pages import connectionpage
from app.pages.connectionpage import ConnectPage
from app.pages import rulepage
from app.pages.rulepage import RulePage
from app.pages import startpage
from app.pages.startpage import StartPage
from kivy.uix.screenmanager import ScreenManager
from kivy.app import App
from kivy.uix.screenmanager import Screen


class SnakeGame(App):
    def build(self):
        self.screen_manager = ScreenManager()

        self.connect_page = ConnectPage()
        screen = Screen(name="Connect")
        screen.add_widget(self.connect_page)
        self.screen_manager.add_widget(screen)

        self.start_page = StartPage()
        screen = Screen(name="Start")
        screen.add_widget(self.start_page)
        self.screen_manager.add_widget(screen)

        self.close_page = ClosePage()
        screen = Screen(name="Close")
        screen.add_widget(self.close_page)
        self.screen_manager.add_widget(screen)

        self.rule_page = RulePage()
        screen = Screen(name="Rule")
        screen.add_widget(self.rule_page)
        self.screen_manager.add_widget(screen)

        self.color_page = ColorPage()
        screen = Screen(name="Color")
        screen.add_widget(self.color_page)
        self.screen_manager.add_widget(screen)

        return self.screen_manager


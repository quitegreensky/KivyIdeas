from kivy.uix.screenmanager import Screen
from kivymd.theming import ThemableBehavior
from kivymd_extensions.akivymd.uix.statusbarcolor import change_statusbar_color


class Home(ThemableBehavior, Screen):
    def on_pre_enter(self, *args):
        change_statusbar_color(self.theme_cls.primary_dark)
        return super().on_enter(*args)

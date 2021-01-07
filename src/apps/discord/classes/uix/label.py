from os import path

from kivy.clock import Clock
from kivy.properties import StringProperty
from kivymd.uix.label import MDLabel

from apps.discord.classes.uix.theme import DiscordTheme


class DiscordLabel(DiscordTheme, MDLabel):
    font_mode = StringProperty("medium")

    fonts_path = "fonts/"
    fonts_def = {"medium": "whitneymedium.otf", "light": "whitneylight.otf"}

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self._update)

    def _update(self, *args):
        font_path = path.join(self.fonts_path, self.fonts_def[self.font_mode])
        self.font_name = font_path

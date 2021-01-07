from kivy.animation import Animation
from kivy.clock import Clock
from kivy.lang.builder import Builder
from kivy.properties import (BooleanProperty, ListProperty, NumericProperty,
                             StringProperty)
from kivy.uix.boxlayout import BoxLayout

from apps.discord.classes.uix.theme import DiscordTheme

Builder.load_string(
    """
<DiscordBottomNavigationIcon>
    orientation: "vertical"
    MDIconButton:
        icon: root.icon
        theme_text_color:"Custom"
        text_color: root.text_color_secondary if root.active else root.light_dark
        valign: "center"
        on_release: root.make_active()
        pos_hint: {"center_x": .5}

<DiscordBottomNavigation>:
    size_hint_y: None
    height: dp(50)

    canvas.before:
        Color:
            rgba:root.almost_black
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: root.radius if root.radius else [0,]

    """
)


class DiscordBottomNavigationIcon(DiscordTheme, BoxLayout):
    active = BooleanProperty(False)
    icon = StringProperty()

    def make_active(self):
        all_buttons = self.parent.children
        for child in all_buttons:
            child.active = False
        self.active = True


class DiscordBottomNavigation(DiscordTheme, BoxLayout):
    radius = ListProperty()
    duration = NumericProperty(0.2)
    transition = StringProperty("out_quad")

    def __init__(self, **kw):
        super().__init__(**kw)
        Clock.schedule_once(self._update)

    def _update(self, *args):
        self.hide()

    def show(self):
        Animation(y=0, d=self.duration, t=self.transition).start(self)

    def hide(self):
        Animation(top=0, d=self.duration, t=self.transition).start(self)

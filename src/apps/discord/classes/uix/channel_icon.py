from kivy.animation import Animation
from kivy.clock import Clock
from kivy.lang.builder import Builder
from kivy.properties import (BooleanProperty, ListProperty, NumericProperty,
                             ObjectProperty, StringProperty)
from kivy.uix.boxlayout import BoxLayout

from apps.discord.classes.uix.theme import DiscordTheme
from classes.uix.scrollview import NoTransitionScrollView

Builder.load_string(
    """
<IconsBar>
    size_hint_x: None
    width: dp(5)

    canvas.before:
        Color:
            rgba: root.text_color_normal
        RoundedRectangle:
            pos: self.pos[0], self.pos[1]+self.height / 2-root._bar_height / 2
            size:  self.size[0], root._bar_height
            radius: [0, root.radius, root.radius, 0]


<DiscordChannelIconsItems>
    size_hint_y: None
    height: dp(55)
    spacing: dp(2)

    IconsBar:
        id: bar

    AnchorLayout:
        anchor_x: "center"
        anchor_y: "center"

        ImageAvatar:
            id: avatar
            source: root.source
            avatar_size: root.height


<DiscordChannelIcons>
    MDBoxLayout:
        id: box
        orientation: "vertical"
        adaptive_height: True
        spacing: dp(10)

    """
)


class IconsBar(DiscordTheme, BoxLayout):
    bar_height = NumericProperty("30dp")
    radius = NumericProperty("6dp")
    _root = ObjectProperty()
    active = BooleanProperty(False)
    _bar_height = NumericProperty()
    transition = StringProperty("out_quad")
    duration = NumericProperty(0.1)

    def __init__(self, **kw):
        super().__init__(**kw)
        Clock.schedule_once(self._update)

    def _update(self, *args):
        self._bar_height = self.bar_height
        self.adjust(self.active)

    def on_active(self, *args):
        self.adjust(self.active)

    def adjust(self, active):
        if active:
            self.expand()
        else:
            self.shrink()

    def shrink(self, *args):
        Animation(_bar_height=self.radius * 2, t=self.transition, d=self.duration).start(self)
        return True

    def expand(self, *args):
        Animation(_bar_height=self.bar_height, t=self.transition, d=self.duration).start(self)
        return True


class DiscordChannelIconsItems(BoxLayout):
    active = BooleanProperty(False)
    source = StringProperty()
    server_name = StringProperty()
    _root = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self._update)

    def _update(self, *args):
        but = self.ids.avatar
        but.bind(on_release=self.set_active)

    def set_active(self, instance):
        bar = self.ids.bar
        all_channels = self._root.ids.box.children
        for child in all_channels:
            child.ids.bar.active = False
        bar.active = True


class DiscordChannelIcons(NoTransitionScrollView):
    def add_widget(self, widget, index=0):
        if issubclass(widget.__class__, DiscordChannelIconsItems):
            self.ids.box.add_widget(widget)
            return True
        return super().add_widget(widget, index=index)

from kivy.lang.builder import Builder
from kivy.properties import StringProperty
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.behaviors import CircularRippleBehavior

from apps.discord.classes.uix.theme import DiscordTheme
from classes.uix.avatar import IconAvatar

Builder.load_string(
    """
<DiscordTextIconButton>
    size_hint: None, None
    size: dp(90), dp(60)
    orientation: "vertical"
    padding: dp(7)

    MDIcon:
        icon: root.icon
        halign: "center"
        valign: "center"
        font_size: dp(25)
        theme_text_color: "Custom"
        text_color: root.text_color_secondary

    DiscordLabel:
        text: root.text
        halign: "center"
        valign: "center"
        font_size: dp(13)
        theme_text_color: "Custom"
        adaptive_height: True
        text_color: root.text_color_secondary


<DiscordTextFieldButton>
    icon: root.icon
    size_hint: None, None
    size: dp(40), dp(40)
    bg_color: root.darkest
    color: root.text_color_secondary
    radius: [self.height / 2, ]
    pos_hint: {"center_y": .5}

    """
)


class DiscordTextIconButton(ButtonBehavior, CircularRippleBehavior, BoxLayout, DiscordTheme):
    icon = StringProperty()
    text = StringProperty()


class DiscordTextFieldButton(DiscordTheme, IconAvatar):
    icon = StringProperty()

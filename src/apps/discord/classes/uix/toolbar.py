from kivy.lang.builder import Builder
from kivy.properties import ListProperty, NumericProperty, StringProperty
from kivymd.uix.button import MDIconButton

from apps.discord.classes.uix.theme import DiscordTheme
from classes.uix.toolbar import CustomToolbar

Builder.load_string(
    """
<DiscordToolbarButton>
    pos_hint: {"center_y": .5}
    theme_text_color: "Custom"
    user_font_size: "25dp"
    text_color: root.text_color_secondary

<DiscordToolbar>
    radius: [root.border_radius,root.border_radius,0,0]
    bg_color: root.light_dark
    height: dp(60)

    CenterToolbarItems:
        DiscordLabel:
            text: root.title
            halign: "left"
            valign: "center"
            theme_text_color: "Custom"
            text_color: root.text_color if root.text_color else root.text_color_normal
            font_size: root.font_size
    """
)


class DiscordToolbarButton(MDIconButton, DiscordTheme):
    pass


class DiscordToolbar(CustomToolbar, DiscordTheme):
    text_color = ListProperty()
    title = StringProperty()
    font_size = NumericProperty("20dp")

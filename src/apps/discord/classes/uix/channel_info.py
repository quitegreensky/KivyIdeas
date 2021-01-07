from kivy.lang.builder import Builder
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout

from apps.discord.classes.uix.theme import DiscordTheme

Builder.load_string(
    """
<DiscordChannelInfo>
    size_hint_y: None
    height: self.minimum_height
    orientation: "vertical"
    padding: dp(20)
    spacing: dp(10)

    MDBoxLayout:
        spacing: dp(10)
        adaptive_height: True

        MDIcon:
            icon: root.icon
            font_size: dp(30)
            theme_text_color: "Custom"
            text_color: root.text_color_secondary
            adaptive_size: True
            halign: "center"
            valign: "center"

        DiscordLabel:
            text: root.text
            halign: "left"
            valign: "center"
            theme_text_color: "Custom"
            text_color : root.text_color_normal
            font_size: dp(23)
            adaptive_height: True

    MDBoxLayout:
        spacing: dp(10)
        adaptive_height: True
        DiscordLabel:
            text: root.description
            halign: "left"
            valign: "center"
            adaptive_height: True
            theme_text_color: "Custom"
            text_color : root.text_color_secondary
            font_size: dp(18)

    """
)


class DiscordChannelInfo(DiscordTheme, BoxLayout):
    text = StringProperty()
    icon = StringProperty("android")
    description = StringProperty()

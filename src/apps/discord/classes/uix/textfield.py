from kivy.lang.builder import Builder
from kivy.properties import StringProperty
from kivymd.uix.textfield import MDTextFieldRound

from apps.discord.classes.uix.theme import DiscordTheme

Builder.load_string(
    """
<DiscordTextField>
    icon_right: "emoticon-happy-outline"
    line_color: root.darkest
    normal_color: root.darkest
    color_active: root.darkest
    hint_text: "Message # support"
    hint_text_color: root.light_dark
    foreground_color: root.text_color_secondary
    icon_right_color: root.text_color_secondary

    """
)


class DiscordTextField(DiscordTheme, MDTextFieldRound):
    pass

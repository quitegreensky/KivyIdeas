from kivy.lang.builder import Builder

from apps.discord.classes.uix.theme import DiscordTheme
from classes.uix.avatar import IconAvatar

Builder.load_string(
    """
    """
)


class DiscordIcon(DiscordTheme, IconAvatar):
    pass

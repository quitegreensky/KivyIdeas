from kivy.clock import Clock
from kivy.properties import ListProperty
from kivy.uix.screenmanager import Screen
from kivymd_extensions.akivymd.uix.statusbarcolor import change_statusbar_color

from apps.discord.classes import registers
from apps.discord.classes.uix.theme import DiscordTheme


class Discord(Screen, DiscordTheme):
    def __init__(self, **kw):
        super().__init__(**kw)
        Clock.schedule_once(self._update)

    def _update(self, *args):
        self.ids.left_menu.channel_list_data = {
            ############################################################
            "KivyMD": {
                "icon": "data/pic/kivymd.png",
                "data": [
                    # =================
                    {
                        "header": {"title": "Community", "icon": "menu"},
                        "channels": [
                            {"title": "support1", "icon": "android"},
                            {"title": "support2", "icon": "android"},
                            {"title": "support3", "icon": "android"},
                        ],
                    },
                    # =================
                    {
                        "header": {"title": "Info", "icon": "menu"},
                        "channels": [{"title": "Whats-new", "icon": "android"}],
                    },
                    # =================
                ],
            },
            ############################################################
            "Kivy": {
                "icon": "data/pic/kivy.png",
                "data": [
                    # =================
                    {
                        "header": {"title": "Community", "icon": "menu"},
                        "channels": [
                            {"title": "support1", "icon": "android"},
                            {"title": "support2", "icon": "android"},
                            {"title": "support3", "icon": "android"},
                        ],
                    },
                    # =================
                    {
                        "header": {"title": "Info", "icon": "menu"},
                        "channels": [{"title": "Whats-new", "icon": "android"}],
                    },
                    # =================
                ],
            },
            ############################################################
        }

        self.ids.right_menu.members = {
            "KIVYMD TEAM": [
                {"title": "KivyMD", "icon": "data/pic/kivymd.png", "color": None},
            ],
            "ONLINE": [
                {"title": "User1", "icon": "data/pic/user.png", "color": None},
                {"title": "User2", "icon": "data/pic/user.png", "color": None},
                {"title": "User3", "icon": "data/pic/user.png", "color": None},
            ],
        }

    def on_pre_enter(self, *args):
        change_statusbar_color(self.darkest)
        return super().on_pre_enter(*args)

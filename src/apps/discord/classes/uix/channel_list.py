from kivy.lang.builder import Builder
from kivy.properties import (DictProperty, ListProperty, ObjectProperty,
                             StringProperty)
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout

from apps.discord.classes.uix.channel_icon import DiscordChannelIconsItems
from apps.discord.classes.uix.theme import DiscordTheme

Builder.load_string(
    """
<DiscordChannelList>
    orientation: "vertical"
    size_hint_y: None
    height: self.minimum_height


<DiscordChannelListItem>:
    size_hint_y: None
    height: dp(30)
    padding: [dp(10),0,0,0]

    MDIcon:
        size_hint_x: None
        width: self.height
        icon: root.icon
        halign: "center"
        valign: "center"
        theme_text_color: "Custom"
        text_color: root.text_color_secondary
        font_size: dp(20)
    
    DiscordLabel:
        text: root.text
        halign: "left"
        valign: "center"
        theme_text_color: "Custom"
        text_color: root.text_color_secondary
        font_size: dp(15)

<DiscordChannelTitle>
    size_hint_y: None
    height: dp(30)

    MDIcon:
        size_hint_x: None
        width: self.height
        icon: root.icon
        halign: "center"
        valign: "center"
        theme_text_color: "Custom"
        text_color: root.text_color_secondary
        font_size: dp(20)
    
    DiscordLabel:
        text: root.text
        halign: "left"
        valign: "center"
        theme_text_color: "Custom"
        text_color: root.text_color_secondary
        font_size: dp(15)

    """
)


class DiscordChannelTitle(DiscordTheme, ButtonBehavior, BoxLayout):
    text = StringProperty()
    icon = StringProperty("android")


class DiscordChannelListItem(DiscordTheme, ButtonBehavior, BoxLayout):
    icon = StringProperty("android")
    text = StringProperty()


class DiscordChannelList(BoxLayout):
    data = DictProperty()
    _root = ObjectProperty()

    def on_data(self, *args):

        for server_name, data in self.data.items():

            server_avatar = DiscordChannelIconsItems(
                source=data["icon"], server_name=server_name, _root=self._root.ids.channels_icon
            )
            self._root.ids.channels_icon.add_widget(server_avatar)

            for cat in data["data"]:
                header = cat["header"]
                channels = cat["channels"]
                self.add_widget(DiscordChannelTitle(text=header["title"], icon=header["icon"]))

                for ch in channels:
                    self.add_widget(DiscordChannelListItem(text=ch["title"], icon=ch["icon"]))

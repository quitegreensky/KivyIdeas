from kivy.lang.builder import Builder
from kivy.properties import DictProperty

from apps.discord.classes.uix.channel_icon import DiscordChannelIcons
from apps.discord.classes.uix.navigation_layout import MenuCardLeft
from apps.discord.classes.uix.theme import DiscordTheme

Builder.load_string(
    """
<LeftMenu>
    canvas.before:
        Color:
            rgba: root.darkest
        Rectangle:
            pos: self.pos
            size: self.size

    BoxLayout:
        size_hint_x: None
        width: dp(80)
        orientation:"vertical"
        id: servers_box
        spacing: dp(10)

        BoxLayout:
            size_hint_y: None
            height: dp(5)

        DiscordIcon:
            size_hint: None, None
            size: [servers_box.width - dp(30),servers_box.width - dp(30)]        
            pos_hint: {"center_x": .5}
            icon: "message"
            bg_color: root.light_dark
            color: root.text_color_secondary
            radius: [servers_box.width - dp(10),]
        
        HorizontalSeparator:
            height: dp(3)
            separator_color: root.light_dark
            pos_hint: {"center_x": .5}
            size_hint_x: None
            width : servers_box.width - dp(30)
            radius: [dp(2),]

        DiscordChannelIcons:
            id: channels_icon

    BoxLayout:
        orientation: "vertical"
        canvas.before:
            Color:
                rgba: root.light_dark
            RoundedRectangle:
                pos: self.pos
                size: self.size
                radius: [root.border_radius,root.border_radius,0,0]

        DiscordToolbar:
            title: "KivyMD"
            LeftToolbarItems:
                DiscordToolbarButton:
                    icon: "menu"


        NoTransitionScrollView:
            DiscordChannelList:
                padding: dp(20)
                spacing: dp(10)
                id: channel_list
                data: root.channel_list_data
                _root: root


    VerticalSeparator:
        width: dp(10)


    """
)


class LeftMenu(MenuCardLeft, DiscordTheme):
    channel_list_data = DictProperty()

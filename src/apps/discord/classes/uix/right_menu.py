from kivy.lang.builder import Builder
from kivy.properties import DictProperty

from apps.discord.classes.uix.members import MemberItem, MembersList, RollTitle
from apps.discord.classes.uix.navigation_layout import MenuCardRight
from apps.discord.classes.uix.theme import DiscordTheme

Builder.load_string(
    """
<RightMenu>

    VerticalSeparator:
        width: dp(10)

    BoxLayout:
        orientation: "vertical"

        MDBoxLayout:
            adaptive_height: True
            orientation: "vertical"

            canvas.before:
                Color:
                    rgba: root.dark
                RoundedRectangle:
                    pos: self.pos
                    size: self.size
                    radius: [root.border_radius,root.border_radius,0,0]

            DiscordChannelInfo:
                text: "support"
                description: "Ask your questions here"

            HorizontalSeparator:
                height: dp(1)
                separator_color: root.light_dark

            MDBoxLayout:
                adaptive_height: True
                BoxLayout:
                DiscordTextIconButton:
                    icon : "magnify"
                    text: "Search"
                DiscordTextIconButton:
                    icon : "bell"
                    text: "Notifications"
                DiscordTextIconButton:
                    icon : "cog"
                    text: "Settings"    
                DiscordTextIconButton:
                    icon : "pin"
                    text: "Pins"                                    
                BoxLayout:
                    
        MembersList:
            id: members
            canvas.before:
                Color:
                    rgba: root.light_dark
                Rectangle:
                    pos: self.pos
                    size: self.size



    """
)


class RightMenu(MenuCardRight, DiscordTheme):
    members = DictProperty()

    def on_members(self, *args):
        member_list = self.ids.members
        members = self.members

        for roll, members_data in members.items():
            title = RollTitle(text=f"{roll} - {len(members_data)}")
            member_list.add_widget(title)

            for user in members_data:
                user_widget = MemberItem(text=user["title"], source=user["icon"])
                if user["color"]:
                    user_widget.text_color = user["color"]
                member_list.add_widget(user_widget)

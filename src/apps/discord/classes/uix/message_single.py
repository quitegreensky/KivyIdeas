from datetime import datetime

from kivy.lang.builder import Builder
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout

from apps.discord.classes.uix.theme import DiscordTheme
from classes.uix.avatar import IconAvatar

Builder.load_string(
    """
#:import get_hex_from_color kivy.utils.get_hex_from_color

<DiscordChatSingle>
    size_hint_y: None
    height: self.minimum_height
    padding: dp(10)

    BoxLayout:
        id: left_bar
        orientation: "vertical"
        size_hint_x: None
        width: dp(55)
        
        ImageAvatar:
            size_hint_y: None
            size: left_bar.width, left_bar.width    
            source: root.source

        BoxLayout:

    BoxLayout:
        orientation: "vertical"
        size_hint_y: None
        height: self.minimum_height


        DiscordLabel:
            text: root.user + "   " + f"[size={int(dp(10))}][color={get_hex_from_color(root.text_color_secondary)}]{root.get_date()}[/color][/size]"
            markup:True
            adaptive_height: True
            halign: "left"
            valign: "center"
            font_size: dp(17)
            theme_text_color: "Custom"
            text_color: self.text_color_normal

        DiscordLabel:
            text: root.message
            adaptive_height: True
            halign: "left"
            valign: "center"
            font_size: dp(15)
            theme_text_color: "Custom"
            text_color: self.text_color_normal
            font_mode: "light"

        BoxLayout:
    """
)


class DiscordChatSingle(DiscordTheme, BoxLayout):
    source = StringProperty("data/pic/user.png")
    user = StringProperty("User")
    message = StringProperty(
        """Test Messsage
        """
    )

    def get_date(self):
        return datetime.now().strftime("%b %d, %Y %H:%M")

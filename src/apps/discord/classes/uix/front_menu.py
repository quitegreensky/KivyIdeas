from kivy.clock import Clock
from kivy.lang.builder import Builder
from kivymd.uix.behaviors import RectangularElevationBehavior

from apps.discord.classes.uix.message_single import DiscordChatSingle
from apps.discord.classes.uix.navigation_layout import MenuCardFront
from apps.discord.classes.uix.theme import DiscordTheme
from classes.uix.scrollview import MessageScrollView

Builder.load_string(
    """
<FrontMenu>
    elevation: 5

    canvas.before:
        Color:
            rgba: root.light_dark
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [root.border_radius, root.border_radius, 0, 0]

    BoxLayout:
        pos: root.pos
        orientation: "vertical"

        DiscordToolbar:
            title: "# support"
            bg_color: root.dark
            id: front_toolbar

            LeftToolbarItems:
                DiscordToolbarButton:
                    icon: "menu"
                    size_hint: None, None
                    size: front_toolbar.height, front_toolbar.height

            RightToolbarItems:
                DiscordToolbarButton:
                    icon: "magnify"
                    size_hint: None, None
                    size: front_toolbar.height, front_toolbar.height

                DiscordToolbarButton:
                    icon: "account-supervisor"
                    size_hint: None, None
                    size: front_toolbar.height, front_toolbar.height

        MessageScrollView:

            MDBoxLayout:
                adaptive_height: True
                id: message_box
                orientation: "vertical"
                BoxLayout:
                    size_hint_y: None
                    height: root.height

        BoxLayout:
            padding: dp(5)
            spacing: dp(10)
            size_hint_y: None
            height: dp(60)
            id: bottom_box

            MDBoxLayout:
                adaptive_width: True
                spacing: dp(10)

                DiscordTextFieldButton:
                    icon: "camera"

                DiscordTextFieldButton:
                    icon: "file"

            BoxLayout:
                padding: [dp(20), dp(5)]

                DiscordTextField:
                    pos_hint: {"center_y": .5}
                    size_hint_y: 1
                    on_text_validate:
                        root.send(self.text)
                        self.text = ""

    """
)


class FrontMenu(RectangularElevationBehavior, MenuCardFront, DiscordTheme):
    reply_message = "Welcome to the channel!"

    def add_message(self, text, user, icon):
        message = DiscordChatSingle(message=text, user=user, source=icon)
        Clock.schedule_once(lambda x: self.ids.message_box.add_widget(message), 0.2)

    def send(self, text):
        self.add_message(text, "Newbie", "data/pic/user.png")
        Clock.schedule_once(
            lambda x: self.add_message(self.reply_message, "KivyMD", "data/pic/kivymd.png"), 2
        )

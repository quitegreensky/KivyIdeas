from kivy.lang import Builder
from kivy.properties import ColorProperty, StringProperty
from kivymd.uix.card import MDCard

Builder.load_string(
    """
<HomeMenuCard>
    size_hint_y: None
    height: dp(100)
    spacing: dp(20)
    padding: dp(20)

    IconAvatar:
        bg_color: root.bg_color
        size_hint: None, None
        size: dp(80), dp(80)
        radius: [self.height/2, ]
        ripple: True
        icon: root.icon
        color: root.icon_color if root.icon_color else app.theme_cls.primary_color
        pos_hint: {"center_y": .5}

    MDLabel:
        text: root.text
        halign: "left"
        valign: "center"

    """
)


class HomeMenuCard(MDCard):
    icon = StringProperty()
    bg_color = ColorProperty()
    icon_color = ColorProperty(None, allownone=True)
    text = StringProperty()

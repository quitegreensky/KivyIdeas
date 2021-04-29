from kivy.lang.builder import Builder
from kivy.properties import ListProperty, ObjectProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout

from classes.uix.scrollview import NoTransitionScrollView

Builder.load_string(
    """
<RollTitle>
    size_hint_y: None
    height: self.minimum_height
    padding: [dp(15), 0]

    DiscordLabel:
        adaptive_height: True
        text: root.text
        theme_text_color: "Custom"
        text_color: root.text_color if root.text_color else self.text_color_secondary
        valign: "center"
        halign: "left"
        font_size: dp(14)


<MembersList>
    MDBoxLayout:
        padding: dp(10)
        orientation: "vertical"
        adaptive_height: True
        id: box


<MemberItem>:
    size_hint_y: None
    height: dp(60)

    ImageAvatar:
        size_hint_x: None
        width: self.height
        source: root.source
        ripple: False

    DiscordLabel:
        text: root.text
        theme_text_color: "Custom"
        text_color: root.text_color if root.text_color else self.text_color_normal
        valign: "center"
        halign: "left"
        font_size: dp(15)
"""
)


class RollTitle(BoxLayout):
    text_color = ListProperty()
    text = StringProperty()


class MemberItem(BoxLayout):
    source = StringProperty()
    text_color = ListProperty()
    text = StringProperty()


class MembersList(NoTransitionScrollView):
    def add_widget(self, widget, index=0):
        if issubclass(widget.__class__, MemberItem) or issubclass(widget.__class__, RollTitle):
            self.ids.box.add_widget(widget)
            return True

        return super().add_widget(widget, index=index)

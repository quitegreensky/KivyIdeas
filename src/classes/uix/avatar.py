from kivy.lang.builder import Builder
from kivy.properties import (BooleanProperty, ListProperty, NumericProperty,
                             StringProperty)
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout
from kivymd.theming import ThemableBehavior
from kivymd.uix.behaviors import CircularRippleBehavior

Builder.load_string(
    """
<AvatarBase>
    _no_ripple_effect: False if root.ripple else True

    canvas.before:
        Color:
            rgba: root.bg_color if root.bg_color else [0, 0, 0, 0]
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: root.radius if root.radius else [0, ]


<IconAvatar>
    MDIcon:
        icon: root.icon
        halign: "center"
        valign: "center"
        theme_text_color: "Custom"
        text_color: root.color if root.color else root.theme_cls.primary_color
        font_size: root.avatar_size if root.avatar_size else self.height*root.avatar_size_hint


<ImageAvatar>
    canvas:
        Color:
            rgba: 1, 1, 1, 1
        RoundedRectangle:
            pos: (self.x + self.width / 2 - root.avatar_size / 2 , \
                self.y + self.height / 2 - root.avatar_size / 2) if root.avatar_size \
                else (self.x + self.width / 2 - self.width * self.avatar_size_hint / 2, \
                    self.y + self.height / 2 - self.height * self.avatar_size_hint / 2)

            size: (root.avatar_size, root.avatar_size) if root.avatar_size else [self.height * self.avatar_size_hint, self.height * self.avatar_size_hint]
            radius: root.radius if root.radius else [0, ]
            source: root.source

    """
)


class AvatarBase(ThemableBehavior, ButtonBehavior, CircularRippleBehavior, BoxLayout):
    color = ListProperty()
    bg_color = ListProperty()
    radius = ListProperty()
    ripple = BooleanProperty(True)
    avatar_size = NumericProperty()
    avatar_size_hint = NumericProperty(0.6)


class IconAvatar(AvatarBase):
    icon = StringProperty("android")


class ImageAvatar(AvatarBase):
    source = StringProperty()

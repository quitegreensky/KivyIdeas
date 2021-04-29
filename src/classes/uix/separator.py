from kivy.lang.builder import Builder
from kivy.properties import ListProperty
from kivy.uix.widget import Widget

Builder.load_string(
    """
<BaseSeparator>
    canvas:
        Color:
            rgba: root.separator_color if root.separator_color else [0, 0, 0, 0]
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: root.radius if root.radius else [0, 0, 0, 0]


<VerticalSeparator>
    size_hint_x: None


<HorizontalSeparator>
    size_hint_y: None

    """
)


class BaseSeparator(Widget):
    separator_color = ListProperty()
    radius = ListProperty()


class VerticalSeparator(BaseSeparator):
    pass


class HorizontalSeparator(BaseSeparator):
    pass

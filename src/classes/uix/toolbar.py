from kivy.lang.builder import Builder
from kivy.properties import ListProperty, NumericProperty, ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.behaviors import RectangularElevationBehavior
from kivymd.uix.boxlayout import MDBoxLayout

Builder.load_string(
    """
<CustomToolbar>
    elevation: 5
    size_hint_y: None
    height: dp(50)
    padding: root.toolbar_padding
    spacing: root.toolbar_spacing

    canvas.before:
        Color:
            rgba: root.bg_color if root.bg_color else [1, 0, 0, 1]
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: root.radius if root.radius else [0, 0, 0, 0]

    MDBoxLayout:
        adaptive_width: True
        id: left_items

    BoxLayout:
        id: center_items

    MDBoxLayout:
        adaptive_width: True
        id: right_items


<RightToolbarItems>
    adaptive_width: True


<LeftToolbarItems>
    adaptive_width: True

    """
)


class RightToolbarItems(MDBoxLayout):
    pass


class LeftToolbarItems(MDBoxLayout):
    pass


class CenterToolbarItems(BoxLayout):
    pass


class CustomToolbar(BoxLayout, RectangularElevationBehavior):
    bg_color = ListProperty()
    radius = ListProperty()
    toolbar_spacing = NumericProperty("5dp")
    toolbar_padding = NumericProperty("5dp")

    def add_widget(self, widget, index=0, canvas=None):
        if issubclass(widget.__class__, RightToolbarItems):
            self.ids.right_items.add_widget(widget)

        elif issubclass(widget.__class__, LeftToolbarItems):
            self.ids.left_items.add_widget(widget)

        elif issubclass(widget.__class__, CenterToolbarItems):
            self.ids.center_items.add_widget(widget)

        else:
            return super().add_widget(widget, index=index, canvas=canvas)

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            super().on_touch_down(touch)
            return True
        else:
            return False

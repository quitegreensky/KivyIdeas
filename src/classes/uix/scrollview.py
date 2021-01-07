from kivy.animation import Animation
from kivy.lang.builder import Builder
from kivy.properties import BooleanProperty, NumericProperty
from kivy.uix.scrollview import ScrollView

Builder.load_string(
    """
#:import ScrollEffect  kivy.effects.scroll.ScrollEffect
<NoTransitionScrollView>
    effect_cls: ScrollEffect
    """
)


class NoTransitionScrollView(ScrollView):
    pass


class MessageScrollView(NoTransitionScrollView):
    animate_scroll = BooleanProperty(True)
    distance_to_move = NumericProperty("10dp")

    def add_widget(self, widget, index=0):
        super().add_widget(widget, index=index)
        self.scroll_y = 0

    def on_touch_move(self, touch):
        if abs(touch.x - touch.ox) > self.distance_to_move:
            self.do_scroll_y = False

        return super().on_touch_move(touch)

    def on_touch_up(self, touch):
        self.do_scroll_y = True
        return super().on_touch_up(touch)

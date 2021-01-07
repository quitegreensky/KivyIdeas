from kivy.animation import Animation
from kivy.clock import Clock
from kivy.event import EventDispatcher
from kivy.lang.builder import Builder
from kivy.properties import (BooleanProperty, NumericProperty, ObjectProperty,
                             StringProperty)
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.relativelayout import RelativeLayout
from kivymd.theming import ThemableBehavior

Builder.load_string(
    """
<MenuCard>
    size_hint_x: None
    width : self._root.width - self._root.back_card_x_space

<CardNavigation>:

    FloatLayout:
        id: back_layout

    FloatLayout:
        id: front_layout

    """
)


class MenuCard(BoxLayout):
    _root = ObjectProperty()


class MenuCardLeft(MenuCard):
    pass


class MenuCardRight(MenuCard):
    pass


class MenuCardFront(BoxLayout):
    x_distance = NumericProperty("15dp")
    _back_layout = ObjectProperty()
    _root = ObjectProperty()
    _x_pos_x = None
    _status = "close"
    front_menu_opacity = NumericProperty(1)

    def on_touch_move(self, touch):
        dis = touch.ox - touch.x

        if self._status == "right" and self.right <= self._root.back_card_x_space and dis > 0:
            return
        elif (
            self._status == "left"
            and self.width - self.x <= self._root.back_card_x_space
            and dis < 0
        ):
            return
        if abs(dis) > self.x_distance and self._status == "close":
            # add right
            current_back = self._current_back()
            if dis > 0:
                if current_back == "left" or not current_back:
                    self._add_panel("right")

            # add left
            else:
                if current_back == "right" or not current_back:
                    self._add_panel("left")
            self.x = touch.x - self._x_pos_x
        elif self._status != "close":
            self.x = touch.x - self._x_pos_x

        return super().on_touch_move(touch)

    def on_touch_down(self, touch):
        self._x_pos_x = touch.x - self.x
        for child in self.children:
            if child.dispatch("on_touch_down", touch):
                return True

        return super().on_touch_down(touch)

    def on_touch_up(self, touch):
        x = touch.x - touch.ox
        if abs(x) > self._root.swipe_distance:
            # move show left
            if x > 0:
                if self._status == "close":
                    self.show_panel("left")
                    self._root.dispatch("on_left_panel")
                elif self._status == "right":
                    self.reset_front()
                    self._root.dispatch("on_front_panel")
                else:
                    self.show_panel("left")

            # show right
            elif x < 0:
                if self._status == "close":
                    self.show_panel("right")
                    self._root.dispatch("on_right_panel")
                elif self._status == "left":
                    self.reset_front()
                    self._root.dispatch("on_front_panel")
                else:
                    self.show_panel("right")

        else:
            if self._status == "close":
                self.reset_front()
            elif self._status == "right":
                self.show_panel("right")
            elif self._status == "left":
                self.show_panel("left")

        return super().on_touch_up(touch)

    def reset_front(self):
        anim = Animation(x=0, t=self._root.transition, d=self._root.anim_duration)
        anim.start(self)
        self._apear_front()
        self._status = "close"
        return True

    def show_panel(self, panel):
        x = self.width - self._root.back_card_x_space
        if panel == "right":
            x *= -1
        elif panel == "left":
            pass
        else:
            Exception("Invalid panel name")
        anim = Animation(x=x, t=self._root.transition, d=self._root.anim_duration)
        anim.start(self)
        Clock.schedule_once(self._fade_front, self._root.anim_duration)
        self._status = panel
        return True

    def _current_back(self):
        back = self._back_layout.children
        if len(back) == 0:
            return False
        if issubclass(back[0].__class__, MenuCardRight):
            return "right"
        elif issubclass(back[0].__class__, MenuCardLeft):
            return "left"

    def _add_panel(self, panel):
        back = self._back_layout
        back.clear_widgets()
        if panel == "right":
            back.add_widget(self._root._rightcard)
        elif panel == "left":
            back.add_widget(self._root._leftcard)
        else:
            raise Exception("invalid panel name")

    def on_size(self, *args):
        if self._status == "close":
            self.reset_front()
        else:
            self.show_panel(self._status)

    def _fade_front(self, *args):
        Animation(opacity=self.front_menu_opacity, t=self._root.transition, d=0.1).start(
            self._root.ids.front_layout
        )

    def _apear_front(self, *args):
        Animation(opacity=1, t=self._root.transition, d=0.1).start(self._root.ids.front_layout)


class CardNavigation(FloatLayout, EventDispatcher):
    back_card_x_space = NumericProperty("60dp")
    swipe_distance = NumericProperty("200dp")
    transition = StringProperty("out_quad")
    anim_duration = NumericProperty(0.2)
    _rightcard = ObjectProperty()
    _leftcard = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.register_event_type("on_right_panel")
        self.register_event_type("on_left_panel")
        self.register_event_type("on_front_panel")

    def on_right_panel(self, *args):
        pass

    def on_left_panel(self, *args):
        pass

    def on_front_panel(self, *args):
        pass

    def add_widget(self, widget, index=0, canvas=None):
        if issubclass(widget.__class__, MenuCardFront):
            widget._root = self
            widget._back_layout = self.ids.back_layout
            self.ids.front_layout.add_widget(widget)
        elif issubclass(widget.__class__, MenuCardRight):
            widget._root = self
            widget.width = self.width - self.back_card_x_space
            widget.right = self.width
            self._rightcard = widget
        elif issubclass(widget.__class__, MenuCardLeft):
            widget._root = self
            widget.width = self.width - self.back_card_x_space
            self._leftcard = widget
        else:
            return super().add_widget(widget, index=index, canvas=canvas)

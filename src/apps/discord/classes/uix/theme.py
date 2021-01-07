from kivy.properties import ListProperty, NumericProperty


class DiscordTheme:
    border_radius = NumericProperty("15dp")
    dark = ListProperty([48 / 255, 49 / 255, 54 / 255, 1])
    darkest = ListProperty([33 / 255, 34 / 255, 39 / 255, 1])
    light_dark = ListProperty([54 / 255, 57 / 255, 64 / 255, 1])
    almost_black = ListProperty([24 / 255, 25 / 255, 29 / 255, 1])
    text_color_normal = ListProperty([1, 1, 1, 1])
    text_color_secondary = ListProperty([195 / 255, 196 / 255, 200 / 255, 1])

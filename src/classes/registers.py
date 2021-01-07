from kivy.factory import Factory

r = Factory.register
r("IconAvatar", module="classes.uix.avatar")
r("ImageAvatar", module="classes.uix.avatar")
r("VerticalSeparator", module="classes.uix.separator")
r("HorizontalSeparator", module="classes.uix.separator")
r("RightToolbarItems", module="classes.uix.toolbar")
r("LeftToolbarItems", module="classes.uix.toolbar")
r("CenterToolbarItems", module="classes.uix.toolbar")
r("CustomToolbar", module="classes.uix.toolbar")
r("NoTransitionScrollView", module="classes.uix.scrollview")

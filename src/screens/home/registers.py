from kivy.factory import Factory

r = Factory.register
path = "screens.home.uix"
r("HomeMenuCard", module=f"{path}.cards")

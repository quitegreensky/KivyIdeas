import json
import sys  # NOQA
from os.path import abspath, dirname, join, relpath, split  # NOQA

from kivy.core.window import Window
from kivy.factory import Factory
from kivy.lang.builder import Builder
from kivymd.app import MDApp
from kivymd_extensions import akivymd

from classes import registers

# sys.path.append(dirname(abspath(__file__))) #NOQA


Window.softinput_mode = "below_target"


class Main(MDApp):
    current_path = dirname(abspath(__file__))
    screen_json_path = join(current_path, "screens.json")

    def build(self):
        return Factory.ScreenManager()

    def show_screen(self, name, mode="next"):
        screenmanager = self.root
        if mode == "next":
            screenmanager.transition.direction = "left"
        elif mode == "previous":
            screenmanager.transition.direction = "right"
        else:
            raise Exception("Invalid show_screen mode")

        if screenmanager.has_screen(name):
            screenmanager.current = name
            return False

        screen = self.open_json(self.screen_json_path)[name]
        path = relpath(screen["path"])
        kv_path = join(path, screen["kv"])
        exec(f"from {self.path_to_import(path)}.{screen['py']} import {screen['cls']}")
        Builder.load_file(kv_path)
        screen_wid = eval(f"Factory.{screen['cls']}(name='{name}')")
        screen_wid.bind(on_leave=self.unload_screen)
        screenmanager.add_widget(screen_wid)
        screenmanager.current = name
        return True

    def unload_screen(self, instance):
        name = instance.name
        screen = self.open_json(self.screen_json_path)[name]
        path = relpath(screen["path"])
        kv_path = join(path, screen["kv"])
        Builder.unload_file(kv_path)
        self.root.remove_widget(instance)
        return True

    def on_start(self):
        self.show_screen("home")
        return super().on_start()

    @staticmethod
    def open_json(path):
        with open(path) as js_file:
            js = json.load(js_file)
        return js

    @staticmethod
    def path_to_import(path):
        path_sp = split(path)
        l = f"".join([f".{p}" for p in path_sp if p])
        return l[1:]


if __name__ == "__main__":
    Main().run()

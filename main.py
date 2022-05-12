from kivy.app import App
from kivymd.app import MDApp
from kivymd.theming import ThemeManager
from kivymd.uix.label import MDLabel

from kivy.properties import ObjectProperty
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView
import cv2
import time

class MenuScreen(Screen):
    pass

class SettingsScreen(Screen):
    pass

class ManuelScreen(Screen):
    pass
class KiScreen(Screen):
    pass


class MainApp(MDApp):
    ben = ObjectProperty()
    taste = ObjectProperty()

    def build(self):
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(SettingsScreen(name='settings'))
        sm.add_widget(ManuelScreen(name='manuel'))
        sm.add_widget(KiScreen(name='ki'))

        return sm

if __name__ == "__main__":
    MainApp().run()


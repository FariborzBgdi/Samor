from kivy.app import App
from kivymd.app import MDApp
from kivymd.theming import ThemeManager
from kivymd.uix.label import MDLabel
from kivymd.uix.picker import MDDatePicker
from kivy.lang import Builder
from kivymd.uix.picker import MDThemePicker
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen

class MenuScreen(Screen):
    pass

class SettingsScreen(Screen):
    pass

class MainApp(MDApp):
    ben = ObjectProperty()
    taste = ObjectProperty()

    def build(self):
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(SettingsScreen(name='settings'))

        return sm

if __name__ == "__main__":
    MainApp().run()

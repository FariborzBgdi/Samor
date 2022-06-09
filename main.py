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

import mqtt_module as mqtt_client

class MenuScreen(Screen):
    pass

class SettingsScreen(Screen):
    def capture(self):
        camera = self.ids['camera']
        timestr = time.strftime("%Y%m%d_%H%M%S")
        camera.export_to_png("IMG_{}.png".format(timestr))
        print("Captured")
    def mecanum_move(self, msg):
        mqtt_client.publish(mqtt_client.TOPIC_MECANUM, msg)
        print("published to mecanum: " + msg)

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
    mqtt_client.connect_to_broker()
    MainApp().run()


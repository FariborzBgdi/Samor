from kivy.app import App
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.theming import ThemeManager
from kivymd.uix.label import MDLabel
from kivy.properties import ObjectProperty
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView
import cv2
import time

#import numpy as np
#import keras
#from keras.applications.vgg16 import VGG16
#from tensorflow.keras.utils import img_to_array
#from keras.applications.imagenet_utils import preprocess_input
#from keras.applications.imagenet_utils import decode_predictions

import mqtt_module as mqtt_client

#model = VGG16(weights='imagenet')

class MenuScreen(Screen):
    pass

class SettingsScreen(Screen):
    def capture(self):
        camera = self.ids['camera']
        timestr = time.strftime("%Y%m%d_%H%M%S")
        camera.export_to_png("IMG_{}.png".format(timestr))
        print("Captured")

        #img_path = "IMG_{}.png".format(timestr)
        #img = keras.utils.load_img(img_path,color_mode='rgb', target_size=(224, 224))
        #x = img_to_array(img)
        #x = np.expand_dims(x, axis=0)
        #x = preprocess_input(x)
        #features = model.predict(x)
        #p = decode_predictions(features)
        #print(p)

    def mecanum_move(self, msg):
        mqtt_client.publish(mqtt_client.TOPIC_MECANUM, msg)
        print("published to mecanum: " + msg)

    def manipulator_move(self, msg):
        mqtt_client.publish(mqtt_client.TOPIC_MANIPULATOR, msg)
        print("published to manipulator: " + msg)

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
    #mqtt_client.connect_to_broker()
    MainApp().run()
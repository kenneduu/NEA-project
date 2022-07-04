import kivy
kivy.require('1.10.0')

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Label
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
##import pandas as pd


##class popUp(Widget):
##    def button(self):
##        popUpFunct()
##
##class P(FloatLayout):
##    pass
##
##def popUpFunct():
##    show = P()
##    window = Popup(title = "Alert!", content = show, size_hint=(None,None), size = (300,00))
##    window.open()
##
##class login(Screen):
##    email = ObjectProperty(None)
##    password = ObjectProperty (None)
##    def validate(self):
##
##        if self.email.text not in users['Email'].unique():
##            PopUpFunct()
##        else:
##            sm.current = 'logdata'
##
##            self.email.text = ""
##            self.password.text = ""



class Thing(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6,0.7)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}

        #return Label(text = 'Hello')

        self.window.add_widget(Image(source='filler.jpeg'))

        self.intro = Label(
                     text="T H E    F E M A L E   N E T W O R K®",
                     font_size=30,
                     color='#4C0121'
                     )
        self.window.add_widget(self.intro)

        self.user = TextInput(
                    multiline=False,
                    padding_y = (20,20),
                    size_hint = (1, 0.5)
                    )

        self.window.add_widget(self.user)

        self.button = Button(
                      text="ENTER",
                      size_hint = (1, 0.5),
                      bold = True,
                      background_color = '#2C041C',
                      background_normal = ""
                      )



        self.button.bind(on_press=self.callback)
        self.window.add_widget(self.button)

        return self.window


    def callback(self, instance):
        self.intro.text = "Hello " +self.user.text + ":D"

if __name__ == '__main__':
    Thing = Thing()
    Thing.run()
    quit()
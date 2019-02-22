from Calculator import *
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty

from kivy.config import Config
Config.set('graphics', 'width', '360')
Config.set('graphics', 'height', '540')


class MainScreen(GridLayout):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        txt_inpt = ObjectProperty(None)
        print(self.txt_inpt.text)
        self.buffer = ""
        self.calc = Calculator()
    def update_label(self, value):
        if (value == "CE"):
            self.buffer = ""
            self.txt_inpt.text = self.buffer
            self.txt_inpt.texture_update()
        elif (value == "C"):
            self.buffer = self.buffer[:len(self.buffer) - 1]
            self.txt_inpt.text = self.buffer
            self.txt_inpt.texture_update()
        else:
            self.buffer += value
            self.txt_inpt.text = self.buffer
            self.txt_inpt.texture_update()
    def do_calculate(self, input):
        self.calc.parser(input)
        self.txt_inpt.text = self.calc.M1
        self.txt_inpt.texture_update()
        self.buffer = self.calc.M1

class MyApp(App):
    def build(self):
        return MainScreen()

if __name__ == '__main__':
    MyApp().run()



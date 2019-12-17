import sys
sys.path.append("../")

import kivy
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout

kivy.require('1.0.6') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label
from elements import map

class TestScreen(GridLayout):
    def __init__(self, **kwargs):
        super(TestScreen, self).__init__(**kwargs)
        #self.cols = 3
        for i in range(9):
            self.add_widget(TextInput(multiline=False, font_size=50, background_color=[1, 1, 3, 1]))

class SecondApp(App):

    def build(self):
        return TestScreen()

if __name__ == '__main__':
    SecondApp().run()
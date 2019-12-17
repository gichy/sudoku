import sys
sys.path.append("../")

import kivy
kivy.require('1.0.6') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label
from elements import map


class MyyApp(App):

    def build(self):
        return Label(text='Hello worlds')


if __name__ == '__main__':
    MyyApp().run()
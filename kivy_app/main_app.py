import sys
sys.path.append("../")

import elements
from elements.map import Map
import kivy
kivy.require('1.0.6') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class SudokuApp(App):

    def build(self):
        return Label(text='Hello worlds')

'''
if __name__ == '__main__':
    MyyApp().run()
'''
def on_text(instance, value):
    print('The widget', instance, 'have:', value)

def set_value(instance, value):
    print("a")
    if value in "123456789":
        instance.field.set_value(int(value))
    for field in instance.parent.children:
        if field != instance and not field.field.fixed:
            show_pot_vals(field)


def show_pot_vals(instance, value="-"):
    #print("a")
    instance.text = "".join([str(x) for x in list(instance.field.potvals)])


class LoginScreen(GridLayout):

    def __init__(self, map, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 9
        self.col_default_width = 20
        bg = lambda x : 30 if ((x%9 < 3 or x%9 > 5) != (x//9 < 3 or x//9 > 5)) else 1
        #for x in range(81):
            #print(x%9 < 3 and x%9 > 5)
            #print(bg(x))
        self.field_widget_list = [TextInput(multiline=False, font_size=50, background_color=[bg(i), bg(i), 3, 1]) for i in range(81)]
        for i, f in enumerate(self.field_widget_list):
            if i % 3 == 0:
                f.border = [0, 30, 0, 30]

            f.field = map.fields[i]
            self.add_widget(f)
            if f.field.fixed:
                f.text = str(f.field.value)
                f.disabled = True
            else:
                f.font_size = 13
                f.field.set_pot_vals()
                f.text = "".join([str(x) for x in list(f.field.potvals)])
                f.bind(on_focus=show_pot_vals)
            f.bind(text=set_value)
        #self.field_widget_list[6].padding = 20
        #self.field_widget_list[5].bind(text=on_text)
        #self.field_widget_list[5].insert_text("4")

        #self.add_widget(Label(text='password'))
        #self.password = TextInput(password=True, multiline=False)
        #self.add_widget(self.password)


class SudokuApp(App):

    def build(self):
        map = Map("/home/agi/suex2.txt")
        return LoginScreen(map)

    def run(self):
        super().run()



if __name__ == '__main__':
    SudokuApp().run()
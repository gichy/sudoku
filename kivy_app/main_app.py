import sys
sys.path.append("../")

import elements
from elements.map import Map
import kivy
kivy.require('1.0.6') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.metrics import cm

def on_text(instance, value):
    print('The widget', instance, 'have:', value)

def set_value(instance, value):
    if value and  value in "123456789":
        instance.field.set_value(int(value))
        for field in instance.parent.parent.children:
            if field.ti_potvals != instance and not field.ti_potvals.field.fixed:
                show_pot_vals(field.ti_potvals)
    else:
        pass
        #instance.field.set_pot_val_set(set([int(s) for s in value]))

def show_pot_vals(instance, value="-"):
    instance.text = "".join([str(x) for x in list(instance.field.potvals)])

class SudokuField(GridLayout):
    def __init__(self, puzzle_screen, field, bgval=0, **kwargs):
        super(SudokuField, self).__init__(**kwargs)
        self.puzzle_screen = puzzle_screen
        self.cols = 1
        bg_img = "../images/FF4D00-0.8.png"
        self.map = map
        self.ti_potvals = SudokuFieldPotVal(bgval, bg_img)
        self.ti = SudokuFieldVal(bgval, bg_img)
        self.ti.field = field
        self.field = field
        self.add_widget(self.ti_potvals)
        self.add_widget(self.ti)
        if field.fixed:
            self.ti.text = str(field.value)
            self.ti.disabled = True
            self.ti_potvals.disabled = True
        else:
            self.ti.text = ""
            self.ti.font_size = 30
            field.set_pot_vals()
            self.ti_potvals.text = "".join([str(x) for x in list(field.potvals)])
            #self.ti_potvals.bind(on_focus=show_pot_vals)
        #self.ti.bind(text=set_value)
        #self.ti_potvals.bind(text=self.set_value)
        self.ti.bind(text=self.set_value)
        self.ti_potvals.bind(text=self.update_pot_vals)
        print(self.ti.text)
        #self.ti_potvals.bind(text=set_value(self.ti, self.ti.text))

    def set_value(self, instance, value):
        if value and value in "123456789":
            print("field " + str(self.field.id) + "has been set to " + str(value))
            self.field.set_value(int(value))
        #    for field in self.puzzle_screen.fields:
        #        if field.ti_potvals != instance and not field.field.fixed:
        #            show_pot_vals(field.ti_potvals)
        #elif value == "":
        #    self.field.set_value(value)
        #else:
        #    instance.field.set_pot_val_set(set([int(s) for s in value]))
        #self.puzzle_screen.sync()

    def update_pot_vals(self, instance, value):
        self.field.update_pot_vals(value)

    def sync(self):
        self.ti.text = str(self.field.value) if self.field.value in range(1,10) else ""
        if not self.field.fixed:
            self.ti_potvals.text = "".join([str(x) for x in list(self.field.potvals)])


class SudokuFieldVal(TextInput):
    def __init__(self, bgval, bg_img, **kwargs):
        super(SudokuFieldVal, self).__init__(**kwargs)
        self.multiline = False
        self.font_size = 30
        self.background_color = [1, 30 if bgval else 1, 3, 2]
        self.background_normal = bg_img
        self.background_disabled_normal = bg_img
        self.background_active = bg_img
        self.size_hint_y = .4
        self.padding = [10, 0, 0, 0]


class SudokuFieldPotVal(TextInput):
    def __init__(self, bgval, bg_img, **kwargs):
        super(SudokuFieldPotVal, self).__init__(**kwargs)
        self.multiline = False
        self.font_size = 8
        self.background_color = [1, 30 if bgval else 1, 3, 2]
        self.background_normal = bg_img
        self.background_disabled_normal = bg_img
        self.background_active = bg_img
        self.size_hint_y = .4

'''
class SudokuFieldTextInput(TextInput):
    def __init__(self, field, bgval=0, **kwargs):
        super(SudokuFieldTextInput, self).__init__(**kwargs)
        self.multiline = False
        self. font_size = 50
        self.background_color = [30 if bgval else 1, 30 if bgval else 1, 3, 1]
        #self.ti = TextInput(multiline=False, font_size=50, background_color=[30 if bgval else 1, 30 if bgval else 1, 3, 1])
        #self.add_widget(self.ti)
        if field.fixed:
            self.text = str(field.value)
            self.disabled = True
        else:
            self.font_size = 13
            field.set_pot_vals()
            self.text = "".join([str(x) for x in list(field.potvals)])
            self.bind(on_focus=show_pot_vals)
'''
class Buttons(BoxLayout):
    def __init__(self, puzzle_screen, **kwargs):
        super(Buttons, self).__init__(**kwargs)
        self.puzzle_screen = puzzle_screen
        self.orientation = "horizontal"
        #self.padding = [20, 20, 20, 20]
        #self.add_widget(Button(size=(cm(10),cm(10))))
        self.add_widget(Button(size_hint_x = .3, text="check_values"))
        self.add_widget(Button(size_hint_x = .2, text="check_potvals"))
        self.add_widget(Button(size_hint_x = .3, text="sync_potvals"))
        sync_all_button = Button(size_hint_x = .2, text="sync all")
        self.add_widget(sync_all_button)
        sync_all_button.bind(on_press=self.sync)

    def sync(self, instance):
        self.puzzle_screen.sync()

class MainScreen(BoxLayout):
    def __init__(self, map, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.orientation = "vertical"
        ps = PuzzleScreen(map)
        self.add_widget(Buttons(ps, size_hint_y = .05))
        self.add_widget(ps)

class PuzzleScreen(GridLayout):

    def __init__(self, map, **kwargs):
        super(PuzzleScreen, self).__init__(**kwargs)
        self.cols = 9
        self.map = map
        self.col_default_width = 20
        bg = lambda x : 1 if ((x%9 < 3 or x%9 > 5) != (x//9 < 3 or x//9 > 5)) else 0
        #for x in range(81):
            #print(x%9 < 3 and x%9 > 5)
            #print(bg(x))
        self.fields = []
        for i in range(81):
            sf = SudokuField(self, map.fields[i], bg(i))
            self.add_widget(sf)
            self.fields.append(sf)
        #self.field_widget_list = [TextInput(multiline=False, font_size=50, background_color=[bg(i), bg(i), 3, 1]) for i in range(81)]
        '''for i, f in enumerate(self.field_widget_list):
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
            f.bind(text=set_value)'''
        #self.field_widget_list[6].padding = 20
        #self.field_widget_list[5].bind(text=on_text)
        #self.field_widget_list[5].insert_text("4")

        #self.add_widget(Label(text='password'))
        #self.password = TextInput(password=True, multiline=False)
        #self.add_widget(self.password)

    def sync(self):
        for field in self.fields:
            field.sync()
        print("potvals for field 8: " + "".join([str(val) for val in self.map.fields[8].potvals]))



class SudokuApp(App):

    def build(self):
        map = Map("/home/agi/suex2.txt")
        return MainScreen(map)

    def run(self):
        super().run()

if __name__ == '__main__':
    SudokuApp().run()
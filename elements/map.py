from col import Col
from field import Field
from row import Row
from distinct import Distinct
from square import Square

class Map:
    def __init__(self, file=""):
        self.fields = [Field(i) for i in range(81)]
        self.cols = [Col(self.fields[i:81:9]) for i in range(9)]
        self.rows = [Row(self.fields[9*i:9*i+9]) for i in range(9)]
        self.squares = [Square(self.fields[i:i+3] + self.fields[i+9:i+12] + self.fields[i+18:i+21]) for i in [0,3,6,27,30,33,54,57,60]]
        self.distincts = self.cols + self.rows + self.squares
        print([[field.id for field in r.fields] for r in self.rows])
        print([[field.id for field in r.fields] for r in self.cols])
        print([[field.id for field in r.fields] for r in self.squares])
        if file:
            i = 0
            with open(file, "r") as f:
                for i, line in enumerate(f):
                    self.rows[i].setRowValues(list(line))
                #i += 1
        print([[field.value for field in r.fields] for r in self.rows])
        self.setValueSets()
        for f in self.fields:
            f.setPotVals()

        while not self.is_full() and (self.naked_single() or self.hidden_single()):
            self.pretty_print()
        self.pretty_print()
        '''changed = True
        while changed:
            changed = False
            self.setValueSets()
            for f in self.fields:
                f.setPotVals()
                #print(len(f.potvals))
                if f.fixed == False and len(f.potvals) == 1:
                    f.setValue(list(f.potvals)[0])
                    changed = True
            print([[field.value for field in r.fields] for r in self.rows])
            self.pretty_print()'''

    def setValueSets(self):
        for c in self.cols:
            c.setValues()
        for c in self.rows:
            c.setValues()
        for c in self.squares:
            c.setValues()

    def naked_single(self):
        changed = False
        for f in self.fields:
            if f.fixed == False and len(f.potvals) == 1:
                f.setValue(list(f.potvals)[0])
                changed = True
        return changed

    def hidden_single(self):
        changed = False
        for d in self.distincts:
            for field, val in d.getHiddenSingles():
                field.setValue(val)
                changed = True
        return changed

    def do_tactic(self):
        pass

    def is_full(self):
        full = True
        for f in self.fields:
            if not f.fixed:
                full = False
        return full

    def pretty_print(self):
        print("/===========\\")
        for i, r in enumerate(self.rows):
            if i ==3 or i == 6:
                print("|===+===+===|")
            print("|" + "".join([f.getPrintableVal() for f in r.fields[0:3]]) +
                  "|" + "".join([f.getPrintableVal() for f in r.fields[3:6]]) +
                  "|" + "".join([f.getPrintableVal() for f in r.fields[6:9]]) + "|")
        print("\===========/")

if __name__ == '__main__':
    map = Map("/home/agi/suex.txt")
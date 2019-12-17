import sys
sys.path.append("../")
import elements


class Field:

    id = None
    row = None
    col = None
    square = None
    value = None
    fixed = False
    potvals = set()

    def __init__(self, id):
        self.id = id

    def set_row(self, row):
        self.row = row

    def set_col(self, col):
        self.col = col


    def set_square(self, square):
        self.square = square


    def set_value(self, val):
        self.value = val
        self.fixed = True
        self.col.drop_pot_val(val)
        self.row.drop_pot_val(val)
        self.square.drop_pot_val(val)
        self.col.setValues()
        self.row.setValues()
        self.square.setValues()
        self.potvals = set([val])

    def set_pot_vals(self):
        #print(self.row.values)
        #print(self.col.values)
        #print(self.square.values)
        #print(set(range(1,10)) - self.row.values - self.col.values - self.square.values)
        self.potvals = set(range(1,10)) - self.row.values - self.col.values - self.square.values

    def drop_pot_val(self, val):
        self.potvals.discard(val)

    def drop_pot_vals(self, vals):
        self.potvals = self.potvals - vals

    def get_printable_val(self):
        return str(self.value) if self.value else "-"
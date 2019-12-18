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
        print("a")
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
        print("potvals len: " + str(len(self.potvals)))
        print("potvals set for field with id " + str(self.id) + ": " + self.get_pot_vals_str())
        self.potvals = set(range(1,10)) - self.row.values - self.col.values - self.square.values

    def update_pot_vals(self, pot_vals_str):
        self.potvals = set(list(pot_vals_str))

    def set_pot_val_set(self, potvals):
        self.potvals = potvals

    def drop_pot_val(self, val):
        print ("potvals before:" + self.get_pot_vals_str())
        print("dropval " + str(val) + " has been dropped for field " + str(self.id))
        self.potvals.discard(val)
        print ("potvals after:" + self.get_pot_vals_str())

    def drop_pot_vals(self, vals):
        self.potvals = self.potvals - vals

    def get_printable_val(self):
        return str(self.value) if self.value else "-"

    def get_pot_vals_str(self):
        return "".join([str(x) for x in list(self.potvals)])
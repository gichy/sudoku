import sys
sys.path.append("../")
import elements


from elements.distinct import Distinct

class Row(Distinct):
    def __init__(self, fields):
        super().__init__(fields)
        for field in self.fields:
            field.set_row(self)

    def set_row_values(self, vals):
        for i, field in enumerate(self.fields):
            if vals[i] != "-":
                field.set_value(int(vals[i]))
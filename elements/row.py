from distinct import Distinct

class Row(Distinct):
    def __init__(self, fields):
        super().__init__(fields)
        for field in self.fields:
            field.setRow(self)

    def setRowValues(self, vals):
        for i, field in enumerate(self.fields):
            if vals[i] != "-":
                field.setValue(int(vals[i]))
from distinct import Distinct

class Col(Distinct):
    def __init__(self, fields):
        super().__init__(fields)
        for field in self.fields:
            field.setCol(self)

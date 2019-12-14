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

    def setRow(self, row):
        self.row = row

    def setCol(self, col):
        self.col = col


    def setSquare(self, square):
        self.square = square


    def setValue(self, val):
        self.value = val
        self.fixed = True
        self.col.dropPotVal(val)
        self.row.dropPotVal(val)
        self.square.dropPotVal(val)
        self.col.setValues()
        self.row.setValues()
        self.square.setValues()
        self.potvals = set([val])

    def setPotVals(self):
        #print(self.row.values)
        #print(self.col.values)
        #print(self.square.values)
        #print(set(range(1,10)) - self.row.values - self.col.values - self.square.values)
        self.potvals = set(range(1,10)) - self.row.values - self.col.values - self.square.values

    def dropPotVal(self, val):
        self.potvals.discard(val)

    def getPrintableVal(self):
        return str(self.value) if self.value else "-"
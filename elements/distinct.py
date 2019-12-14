class Distinct():
    def __init__(self, fields):
        self.fields = fields

    def setValues(self):
        self.values = set()
        for f in self.fields:
            if f.fixed:
                self.values.add(f.value)

    def getHiddenSingles(self):
        self.setValues()
        hs = {v : 0 for v in (set(range(1,10)) - self.values)}
        for f in self.fields:
            if not f.fixed:
                for pv in f.potvals:
                    if pv in hs:
                        if hs[pv] == 0:
                            hs[pv] = f
                        else:
                            hs.pop(pv)
        for k,v in hs.items():
            if v == 0:
                hs.pop(k)
        return [(field,val) for val,field in hs.items()]

    def dropPotVal(self, val):
        for f in self.fields:
            f.dropPotVal(val)
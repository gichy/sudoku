import sys
sys.path.append("../")
import elements


class Distinct():
    def __init__(self, fields):
        self.fields = fields

    def setValues(self):
        self.values = set()
        for f in self.fields:
            if f.fixed:
                self.values.add(f.value)

    def get_hidden_singles(self):
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

    def drop_pot_val(self, val):
        for f in self.fields:
            f.drop_pot_val(val)

    def find_naked_pairs(self):
        np = []
        res = []
        for field in self.fields:
            if not field.fixed:
                if len(field.potvals) == 2 and field.potvals in np:
                    res.append(field.potvals)
                elif len(field.potvals) == 2:
                    np.append(field.potvals)
        if res:
            print("np found")
            print(", ".join([str(field.id) for field in self.fields]))
            for r in res:
                print(", ".join([str(potval) for potval in r]))
        return res

    def do_naked_pairs_drop(self):
        naked_pairs = self.find_naked_pairs()
        for np in naked_pairs:
            for field in self.fields:
                if not field.fixed and np != field.potvals:
                    print("potvals being dropped here: " + str(field.id))
                    print("original potvals:")
                    print(field.potvals)
                    field.drop_pot_vals(np)
                    print("new potvals:")
                    print(field.potvals)


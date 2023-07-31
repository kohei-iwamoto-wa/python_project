import json

class JsonManager:
    def __init__(self, data):
        self.data = data
        
    def loads(self):
        return json.loads(self.data)

    def dump(self):
        return json.dump(self.data)

s = '{"A": {"X": 1, "Y": 1.0, "Z": "abc"}, "B": [true, false, null, NaN, Infinity]}'

ins = JsonManager(s)
a = ins.load()
print(a)
ins = JsonManager(a)
b = ins.dump()
print(b)
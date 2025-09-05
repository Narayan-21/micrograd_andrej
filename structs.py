from viz import draw_dot

class Value:
    def __init__(self, data, _children=(), _op="", label=""):
        self.data = data
        self.grad = 0.0
        self._prev = set(_children)
        self._op = _op
        self.label = label
        
    def __repr__(self):
        return f"Value(data={self.data})"

    def __add__(self, other):
        out = Value(self.data+other.data, (self, other), "+")
        return out
    
    def __mul__(self, other):
        out = Value(self.data * other.data, (self, other), "*")
        return out

a = Value(2.0, label="a")
b = Value(-3.0, label="b")
c = Value(10.0, label="c")
e = a*b; e.label="e"
d = e+c; d.label="d"
f = Value(-2.0, label="f")
L = d*f; L.label="L"    

L.grad = 1.0


def lol():
    h = 0.0001
    
    a = Value(2.0, label="a")
    b = Value(-3.0, label="b")
    c = Value(10.0, label="c")
    e = a*b; e.label="e"
    d = e+c; d.label="d"
    f = Value(-2.0, label="f")
    L = d*f; L.label="L"
    L1 = L.data
    
    L.grad = 1
    a = Value(2.0, label="a")
    b = Value(-3.0, label="b")
    c = Value(10.0, label="c")
    e = a*b; e.label="e"
    d = e+c; d.label="d"
    f = Value(-2.0, label="f")
    L = d*f; L.label="L"
    L2 = L.data
    f.grad = 4.0
    d.grad = -2.0
    c.grad = -2.0
    e.grad = -2.0
    a.grad = 6.0
    b.grad = -4.0
    print((L2 - L1) / h)
    return L

# lol()
draw_dot(lol())

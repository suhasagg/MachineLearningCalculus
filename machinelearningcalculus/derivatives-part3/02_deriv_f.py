from sympy import diff, sin, pprint
from sympy.abc import x

u = x**2
v = sin(x)
f = u * v
result = diff(f, x)
print("Derivative of")
pprint(f)
print("with respect to x is")
pprint(result)

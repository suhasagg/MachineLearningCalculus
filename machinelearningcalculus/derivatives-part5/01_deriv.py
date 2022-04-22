from sympy.abc import x, y
from sympy import diff, pprint

f = x**2 + 2 * y**2
dx = diff(f, x)
dy = diff(f, y)
print("Derivative of")
pprint(f)
print("with respect to x is")
pprint(dx)
print("and with respect to y is")
pprint(dy)

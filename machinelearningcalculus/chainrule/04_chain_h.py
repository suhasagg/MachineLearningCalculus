from sympy.abc import x, y
from sympy import diff, pprint

s = x*y
t = 2*x - y
h = s**2 + t**3
dhdx = diff(h, x)
dhdy = diff(h, y)
print("Function")
pprint(h)
print("Derivative with respect to x")
pprint(dhdx)
print("Derivative with respect to y")
pprint(dhdy)

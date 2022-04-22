from sympy.abc import x, y
from sympy import diff, sqrt, cos, simplify, pprint

u = x * sqrt(x**2 - 10)
h = cos(u)
result = diff(h, x)
print("Function")
pprint(h)
print("has derivative")
pprint(simplify(result))

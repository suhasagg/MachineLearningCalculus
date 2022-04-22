from sympy import diff, sin, pprint
from sympy.abc import x

f = -x * sin(x)
d1 = diff(f, x)
d2 = diff(f, x, x)
print("Function")
pprint(f)
print("has first derivative")
pprint(d1)
print("and second derivative")
pprint(d2)

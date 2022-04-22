from sympy import diff, sin, cos, simplify, pprint
from sympy.abc import x

f = sin(x) / cos(x)
result = diff(f, x)
print("Derivative of")
pprint(f)
print("with respect to x is")
pprint(simplify(result))

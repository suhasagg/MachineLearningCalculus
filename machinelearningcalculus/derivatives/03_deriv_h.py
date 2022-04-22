from sympy import diff, sqrt, pprint
from sympy.abc import x

expression = 1/x
result = diff(expression, x)
print("Derivative of")
pprint(expression)
print("with respect to x is")
pprint(result)

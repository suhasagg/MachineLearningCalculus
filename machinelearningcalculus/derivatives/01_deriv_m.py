from sympy import diff, sqrt, pprint
from sympy.abc import x

expression = 2*x + 5
result = diff(expression, x)
print("Derivative of")
pprint(expression)
print("with respect to x is")
pprint(result)

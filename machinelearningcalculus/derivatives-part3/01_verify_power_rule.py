from sympy import diff, sqrt, pprint
from sympy.abc import x

expressions = [x**2, sqrt(x)]
for expression in expressions:
    result = diff(expression, x)
    print("Derivative of")
    pprint(expression)
    print("with respect to x is")
    pprint(result)
    print()

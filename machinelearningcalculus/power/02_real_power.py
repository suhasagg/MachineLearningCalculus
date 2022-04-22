from sympy import diff, pprint, powsimp, simplify
from sympy.abc import x

expressions = ["k*x**a", "x**0.2", "x**pi", "x**(-3/4)"]
for expression in expressions:
    expression = simplify(expression)
    result = diff(expression, x)
    print("Derivative of")
    pprint(expression)
    print("with respect to x is")
    pprint(powsimp(result))
    print()

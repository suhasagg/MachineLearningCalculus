from sympy.abc import x, y, p, q, r, s, t, u
from sympy import exp, Matrix, simplify, pprint

def sigmoid(x):
    return 1/(1+exp(-x))

# Vector-valued function
f = Matrix([sigmoid(p*x+q*y), sigmoid(r*x+s*y), sigmoid(t*x+u*y)])
variables = Matrix([x,y])
# Find and print the Jacobian
pprint(f.jacobian(variables))

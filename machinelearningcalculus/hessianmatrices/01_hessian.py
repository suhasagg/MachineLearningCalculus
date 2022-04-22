from sympy.abc import x, y
from sympy import pprint, hessian

g = x**3 + 2*y**2 + 3*x*y**2
variables = [x, y]
h = hessian(g, variables)
d = h.det()
print("Function")
pprint(g)
print("Hessian")
pprint(h)
print("Discriminant")
pprint(d)
for xval,yval in [(0,0), (1,0), (0,1), (-1,0)]:
    val = d.subs([(x,xval),(y,yval)])
    print(f"Discriminant at ({xval},{yval}) = {val}")

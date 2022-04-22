import numpy as np
from scipy.optimize import minimize

def objective(x):
    return x[0]**2 + x[1]**2

def constraint(x):
    return x[0]+2*x[1]-1

# initial guesses
x0 = np.array([3,3])

# optimize
bounds = ((-10,10), (-10,10))
constraints = [{"type":"eq", "fun":constraint}]
solution = minimize(objective, x0, method='SLSQP', bounds=bounds, constraints=constraints)
x = solution.x

# show solution
print('Objective:', objective(x))
print('Solution:', x)

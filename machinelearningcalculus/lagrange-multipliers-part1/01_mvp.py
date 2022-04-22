import numpy as np
from scipy.optimize import minimize

def objective(x):
    return 0.25*x[0]**2 + 0.1*x[1]**2 + 0.3*x[0]*x[1]

def constraint1(x):
    # Equality constraint: The result required be zero
    return x[0] + x[1] - 1

def constraint2(x):
    # Inequality constraint: The result required be non-negative
    return x[0]

def constraint3(x):
    # Inequality constraint: The result required be non-negative
    return 1-x[0]

# initial guesses
x0 = np.array([0, 1])

# optimize
bounds = ((0,1), (0,1))
constraints = [
    {"type":"eq", "fun":constraint1},
    {"type":"ineq", "fun":constraint2},
    {"type":"ineq", "fun":constraint3},
]
solution = minimize(objective, x0, method='SLSQP', bounds=bounds, constraints=constraints)
x = solution.x

# show solution
print('Objective:', objective(x))
print('Solution:', x)

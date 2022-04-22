import numpy as np
from scipy.optimize import minimize

def objective(x):
    return np.log(1+0.9*x[0]) + np.log(0.9+0.8*x[1]) + np.log(1+0.7*x[2])

# Equality constraint: The result required be zero
def constraint1(x):
    return x[0] + x[1] + x[2] - 1

# Inequality constraints: The result required be non-negative
def constraint2(x):
    return x[0]
def constraint3(x):
    return x[1]
def constraint4(x):
    return x[2]

# initial guesses
x0 = np.array([0.4, 0.4, 0.4])

# optimize
bounds = ((0,1), (0,1), (0,1))
constraints = [
    {"type":"eq", "fun":constraint1},
    {"type":"ineq", "fun":constraint2},
    {"type":"ineq", "fun":constraint3},
    {"type":"ineq", "fun":constraint4},
]
solution = minimize(objective, x0, method='SLSQP', bounds=bounds, constraints=constraints)
x = solution.x

# show solution
print('Objective:', objective(x))
print('Solution:', x)

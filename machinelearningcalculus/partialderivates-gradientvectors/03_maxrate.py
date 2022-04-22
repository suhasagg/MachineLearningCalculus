import numpy as np

def f(x, y):
    return x**2 + y**2

x, y = 1, 1
step = 0.001
angles = np.arange(0, 360, 5) # 0 to 360 degrees at 5-degree steps
maxdf, maxangle = -np.inf, 0
for angle in angles:
    rad = angle * np.pi / 180 # convert degree to radian
    dx, dy = np.sin(rad)*step, np.cos(rad)*step
    df = (f(x+dx, y+dy) - f(x,y))/step
    if df > maxdf:
        maxdf, maxangle = df, angle
    print(f"Rate of change at {angle} degrees = {df}")

dx, dy = np.sin(maxangle*np.pi/180), np.cos(maxangle*np.pi/180)
gradx, grady = dx*maxdf, dy*maxdf
print(f"Max rate of change at {maxangle} degrees")
print(f"Gradient vector at ({x},{y}) is ({dx*maxdf},{dy*maxdf})")

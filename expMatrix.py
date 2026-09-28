from functions import ODE
import numpy as np
from scipy.linalg import expm
import sys

"""
    Raise e to the power of a matrix and map the vector field
"""

## Input: Array
A = np.array([[0, 1],
              [-1, 0]])
print(f'Array:\n{A}\n')

# Input: Time
timestep = 0.5 # Time step
duration = 2


# ========================================================================================
ode = ODE(duration, timestep)

# Multiply
for t in ode.time:
    # if t == 0:
    #     continue
    v = expm(A*t)
    print(f'Time: {t}')
    print(f'{v}\n')


# time = np.linspace(0, 2*np.pi, 10)
# matrix = np.array([[0, -1], [1, 0]])
# time = np.linspace(0, 2*np.pi, 10)
# for t in time:
#     # print(expm(matrix * t))
#     M = expm(matrix * t)
#     angle = np.arctan2(M[1, 0], M[0, 0])
#     print(f'Angle at time {round(t,2)}: {round(angle,3)}')

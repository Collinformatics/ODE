from functions import ODE
import numpy as np
import pandas as pd
import sys


# Input: Time
timestep = 0.05 # Time step
duration = 2
time = np.arange(0, duration+timestep, timestep)
nDatapoints = len(time)

# Input: Equation
a = 4
k = -5


# ========================================================================================
def exponential(A, rate, x):
    return A*np.exp(rate*x)

y = exponential(a, k, time)


# Equation label
label = ''
if a != 1:
    label += f'{a}*'
if k != 1:
    label += f'e^{{{k}*t}}'
else:
    label += f'e^{{t}}'
label = f'${label}$'


# Apply Euler's Method
diff1 = np.gradient(y)
diff2 = np.gradient(diff1)
diff3 = np.gradient(diff2)
diff4 = np.gradient(diff3)
sets = {}
for i in range(1,1):
    d = np.gradient(d)
    sets['labels'] = f'{i} Taylor Expansion'
    sets['y(h)'].append([])
    sets['time'].append(time)





# ========================================================================================
def TaylorExpansion(step_h):
    t_taylor = np.arange(0, duration + h, h)
    y_taylor = (y[0] + diff1[0] * t_taylor +
                diff1[0] * (t_taylor**2)/2 +
                diff2[0] * (t_taylor**3)/3 +
                diff3[0] * (t_taylor**4)/4)
    return t_taylor, y_taylor

# Build the Taylor approximation
h = 0.1
tayor_t, tayor_y = TaylorExpansion(step_h=h)

# DataFrame
data = pd.DataFrame({
    'Time':  np.concatenate([time, tayor_t]),
    'y(t)': np.concatenate([y, tayor_y]),
    'y': ['Exact'] * len(time) + [f'Taylor (h={h})'] * len(tayor_y),
})

ode = ODE
ode.plotLines(data)
# Plot data


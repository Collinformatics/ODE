from functions import ODE
import math
import numpy as np
import pandas as pd
import sys


# Input: Time
timestep = 0.05 # Time step
duration = 2

# Input: Equation
a = 4
k = -5


# ========================================================================================
# Equation label
label = ''
if a != 1:
    label += f'{a}*'
if k != 1:
    label += f'e^{{{k}*t}}'
else:
    label += f'e^{{t}}'
label = f'${label}$'

# Set options
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 10)
pd.set_option('display.width', 1000)
pd.set_option('display.float_format', '{:,.2f}'.format)


# ========================================================================================
# Initialize class
ode = ODE(duration, timestep)

# Create trendline
def exponential(A, rate, x):
    return A*np.exp(rate*x)
y = exponential(a, k, ode.time)

# Prep dataframe
data = pd.DataFrame(0.0, index=ode.time, columns=[])
data[label] = y
print(f'Taylor:\n{data}\n')

def TaylorExpansion(yValues, duration, h):
    diff1 = np.gradient(yValues)
    diff2 = np.gradient(diff1)
    diff3 = np.gradient(diff2)
    diff4 = np.gradient(diff3)

    time = np.arange(0, duration + h, h)
    time = ode.time
    yTaylor = []
    for i in range(1, len(time)-1):
        yTaylor = (
                y[i] +
                diff1[i] * time[i] +
                diff2[i] * (time[i]**2)/math.factorial(2) +
                diff3[i] * (time[i]**3)/math.factorial(3) +
                diff4[i] * (time[i]**4)/math.factorial(4)
        )
    df = pd.DataFrame(0.0, index=time, columns=[])
    df['Taylor'] = yTaylor
    print(f'Taylor Expansion:\n{df}\n')
    return yTaylor, df


# Build the Taylor approximation
h = 0.1
label2 = f'Taylor (h={h})'
tayorY, df = TaylorExpansion(yValues=y, duration=duration, h=h)
data[label2]  = tayorY

# Plot data
ode.plotLines(
    data=data, colors=['black', '#7700AA', '#20BB20'],
    title='Taylor Expansion', labelX='Time', labelY='y(t)'
)

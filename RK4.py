from functions import ODE
import numpy as np
import pandas as pd
import random


"""
    Use Runge-Kutta to approximate a curve
"""


# Input: Curve Params
inA = 0.1
inB = 0
inK = 0.5
inDeviation = 0.5

# Input: Time
inTimestep = 0.01 # Time step
inDatapoints = 1

# Figure params
inColors = ['black','green']
inFigName = 'runge_kutta4'
inBrowserFig = False


# ========================================================================================
def exponential(x):
    return np.exp(x)


def genCurve(timepoints, A, b, k,  error):
    d = pd.DataFrame(0.0, index=[], columns=['y'])
    for t in timepoints:
        # val = (A * np.exp(x * k) + b) + random.uniform(0, error)
        d.loc[t, 'y'] = exponential(t) + random.uniform(0, error)
    return d


# ========================================================================================
# Initialize class
ode = ODE(duration=inDatapoints, timestep=inTimestep)

# Generate data
# data = ode.genCurve(timepoints=ode.time, A=inA, k=inK, b=inB, error=inDeviation)
data = pd.DataFrame()
data = ode.rk4(curve=data)

# Plot data
if inBrowserFig:
    ode.plotLines(
        data=data, colors=inColors, title='Runge-Kutta 4',
        labelX='Time', labelY='y(t)', browserFig=inFigName
    )
else:
    ode.plotLines(
        data=data, colors=inColors, title='Runge-Kutta 4',
        labelX='Time', labelY='y(t)', browserFig=False
    )

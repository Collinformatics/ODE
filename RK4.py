from functions import ODE
import numpy as np
import pandas as pd
import random


"""
    Use Runge-Kutta to approximate a curve
"""


# Input: Curve Params
inA = 0.05
inB = -0.75
inK = 1
inDeviation = 0.5

# Input: Time
inTimestep = 0.1 # Time step
inDatapoints = 5

# Figure params
inColors = ['green', 'black']
inFigName = 'runge_kutta'
inFigName = False


# ========================================================================================
def expCurve(xValues, A, b, k,  error):
    d = pd.DataFrame(0.0, index=[], columns=['y'])
    for x in xValues:
        val = (A * np.exp(x * k) + b) + random.uniform(0, error)
        d.loc[x + 1, 'y'] = val
    return d


# ========================================================================================
# Initialize class
ode = ODE(duration=inDatapoints, timestep=inTimestep)

# Generate data
data = expCurve(xValues=ode.time, A=inA, k=inK, b=inB, error=inDeviation)
data = ode.rk4(curve=data)

# Plot data
ode.plotLines(
    data=data, colors=inColors, title='Runge-Kutta 4', labelX='Time', labelY='y(t)',
    browserFig=inFigName
)


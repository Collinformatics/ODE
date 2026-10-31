from functions import ODE
import pandas as pd


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
# Set options
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
pd.set_option('display.float_format', '{:,.2f}'.format)

# Initialize class
ode = ODE(duration=inDatapoints, timestep=inTimestep)


# ========================================================================================
data = ode.expCurve(A=inA, k=inK, b=inB, error=inDeviation)
data = ode.rk4(curve=data)

# Plot data
ode.plotLines(
    data=data, colors=inColors, title='Runge-Kutta 4', labelX='Time', labelY='y(t)',
    browserFig=inFigName
)


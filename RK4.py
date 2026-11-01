from functions import ODE
import numpy as np


"""
    Use Runge-Kutta 4 to solve an ODE by approximate the solution of a first-order ODE.
    
    This allows us to start with a function that describes the change:
        y' = f(t, y)
    
    and find a function that makes the first derivative true:
        y(t)

    Steps forward from an initial condition y(t_0) = y_0 in increments of h.
    Approximate y(t) at discrete time points by averaging four slope estimates per step. 
    
    Returns an array of (t, y) values.
"""


# Input: Time
inTimestep = 0.01 # Time step
inDatapoints = 5

# Figure params
inColors = ['green']
inFigName = 'runge_kutta4'
inBrowserFig = True

# Input: 1st Derivative
inInitY = 0
def firstDerivative(t, y):
    return np.tan(2*t) - t*np.exp(np.sin(y))


# ========================================================================================
# Initialize class

ode = ODE(duration=inDatapoints, timestep=inTimestep)

# Solve
data = ode.rk4(f=firstDerivative, h=inTimestep, y0=inInitY)

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

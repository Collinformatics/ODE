import numpy as np
import pandas as pd
from plotnine import *
import sys


# Input: Time
timestep = 0.01 # Time step
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


# for h in [timestep*5, timestep*3, timestep*2]:
tayor = []
for h in [0.05]:
    for t in np.arange(0, duration+h, h):
        tayor.append(y[0] + diff1[0]*t)


# ========================================================================================
# Build the Taylor approximation
tayor_t = np.arange(0, duration + h, h)
tayor_y = y[0] + diff1[0] * tayor_t + diff1[0] * (tayor_t**2)/2

# Long-format DataFrame
data = pd.DataFrame({
    'Time':  np.concatenate([time, tayor_t]),
    'y(t)': np.concatenate([y, tayor_y]),
    'Series': ['Exact'] * len(time) + [f'Taylor (h={h})'] * len(tayor_y),
})
tayor_data = data[data['Series'] == f'Taylor (h={h})']
p = (
        ggplot(data, aes(x='Time', y='y(t)', colour='Series', linetype='Series'))
        + geom_line(size=0.75) # Line width
        + geom_point(data=tayor_data, shape=10, size=3) # diamonds on Taylor only
        + scale_color_manual(values={'Exact': '#101010', f'Taylor (h={h})': '#20BB20'})
        + scale_linetype_manual(values={'Exact': 'solid', f'Taylor (h={h})': 'dashed'})
        + labs(title='Taylor Expansion')
        + theme_bw()
        + theme(
    figure_size=(8, 5),
    plot_title=element_text(size=16, face='bold'),
    axis_title_x=element_text(size=14),
    axis_title_y=element_text(size=14, rotation=0),
    axis_text=element_text(size=12),
    strip_background=element_blank(),
    panel_border=element_rect(color='black', fill=None),
    panel_grid_major=element_line(color='black', size=0.25),
)
)
p.show()
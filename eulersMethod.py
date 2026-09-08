import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
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

# Long-format DataFrame
data = pd.DataFrame({
    'Time':  np.concatenate([time, tayor_t]),
    'y(t)': np.concatenate([y, tayor_y]),
    'y': ['Exact'] * len(time) + [f'Taylor (h={h})'] * len(tayor_y),
})


# Plot data
fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(time, y, color='#101010', linewidth=1.5, label=label)
ax.plot(tayor_t, tayor_y, color='#20BB20', linewidth=0.75, linestyle='--',
        label=f'Taylor (h={h})')
ax.scatter(tayor_t, tayor_y, marker='D', s=20, color='#20BB20', zorder=5)
ax.legend(loc='best', framealpha=0.8)

# Styling
ax.set_title('Taylor Expansion', fontsize=16, fontweight='bold')
ax.set_xlabel('Time', fontsize=14)
ax.set_ylabel('y(t)', fontsize=14, rotation=0, labelpad=20)
ax.tick_params(labelsize=12)

# Grid
ax.grid(True, linewidth=0.25, color='black')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.show()

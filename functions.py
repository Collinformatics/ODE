import jax
import os
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import numpy as np
import pandas as pd
import random
import sys


# Set options
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 10)
pd.set_option('display.width', 1000)
pd.set_option('display.float_format', '{:,.2f}'.format)

# GPU Usage
# print(f'Jax Device: {jax.default_backend()}')


def pressKey(event):
    if event.key == 'escape':
        plt.close()
    elif event.key == 'e':
        sys.exit()
    elif event.key == 'r':
        python = sys.executable
        os.execl(python, python, *sys.argv)


def getAxisTicks(values, largeValues=True, customSteps=None):
    if customSteps is None:
        customSteps = []
    padding = 0.05
    if not isinstance(values, list):
        values = list(values)
    if customSteps is not None:
        steps = customSteps
    else:
        if largeValues:
            steps = [25, 20, 30, 40, 50]
        else:
            steps = [5, 2, 3, 4]
            padding = 0.01

    dist = values[-1] - values[0]
    padding = int(padding * dist)
    ticks = []
    for step in steps:
        if dist % step == 0:
            ticks = list(np.arange(values[0], values[-1] + step, step))
            print(f'Step: {step}')
            break
    # print(f'xTicks: {ticks}\n')
    return ticks, padding


class ODE:
    def __init__(self, duration, timestep):
        self.time = np.arange(0, duration+timestep, timestep)
        self.printN = 10

        # Params: Figures
        self.figDir = 'Figures'
        self.figSize = (9.5, 8) # (width, height)
        self.figSizeWide = (9.5, 5)
        self.labelSizeTitle = 20 # Set font-size
        self.labelSizeAxis = 16 # Set font-size
        self.labelSizeTicks = 12 # Set font-size
        self.lineThickness = 1.5
        self.tickLength = 4
        self.figureResolution = 600

        if not os.path.exists(self.figDir):
            os.makedirs(self.figDir, exist_ok=True)


    def genCurve(self, error):
        d = pd.DataFrame(0.0, index=[], columns=['y'])
        for t in self.time:
            d.loc[t, 'y'] = self.f(t) + random.uniform(0, error)
        return d


    @staticmethod
    def f(x):
        return x**3


    @staticmethod
    def differentiate(self, f):
        df_dt = jax.grad(f)


    def rk4(self, f, h, y0):
        print(f'Runge-Kutta')
        d = pd.DataFrame(0.0, index=self.time, columns=['RK4'])

        def step(t, y):
            k1 = f(t, y)
            k2 = f(t + h/2, y + h/2 * k1)
            k3 = f(t + h / 2, y + h / 2 * k2)
            k4 = f(t + h / 2, y + h * k3)
            return y + h/6 * (k1 + 2*k2 + 2*k3 + k4)

        # Evaluate
        y = y0
        for i, t in enumerate(d.index):
            d.loc[t, 'RK4'] = y
            y = step(t, y)
        print(f'Data:\n{d}\n')
        return d


    def plotLines(self, data, colors, title,
                  labelX, labelY, yRotate=0, browserFig=False):
        fig, ax = plt.subplots(figsize=self.figSize)
        for i in range(data.columns.size):
            ax.plot(data.index, data.iloc[:,i], color=colors[i],
                    label=data.columns[i], linewidth=self.lineThickness)
        ax.legend(fontsize=self.labelSizeTicks, loc='best',
                  edgecolor='black', framealpha=0.8)

        # Styling
        ax.set_title(title, fontsize=self.labelSizeTitle, fontweight='bold')
        ax.set_xlabel(labelX, fontsize=self.labelSizeAxis)
        ax.set_ylabel(labelY, fontsize=self.labelSizeAxis, labelpad=20, rotation=yRotate)
        ax.tick_params(labelsize=12)

        # Axis params
        xTicks, pad = getAxisTicks(values=data.index)
        if xTicks:
            ax.set_xlim(data.index[0]-pad, data.index[-1]+pad)
            ax.set_xticks(xTicks)
        else:
            ax.xaxis.set_major_locator(MaxNLocator(integer=True))
        ax.yaxis.set_major_locator(MaxNLocator(integer=True))
        if max(ax.get_ylim()) > 1:
            ax.set_ylim(top=int(np.ceil(ax.get_ylim()[1])))

        # Grid
        ax.grid(True, linewidth=0.25, color='black')
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)

        for _, spine in ax.spines.items():
            spine.set_visible(True)

        plt.tight_layout()
        if browserFig:
            import subprocess

            # Save figure
            savePath = os.path.join(self.figDir, f'{browserFig}.png')
            plt.savefig(savePath, bbox_inches='tight')
            print(f'Figure was saved at path:\n\t{savePath}\n')
            subprocess.run(['xdg-open', savePath])  # Open fig in web browser
        else:
            fig.canvas.mpl_connect('key_press_event', pressKey)
            plt.show()
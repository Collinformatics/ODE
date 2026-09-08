import matplotlib as mpl
import matplotlib.pyplot as plt

class ODE:
    def __init__(self):
        self.printN = 10

        # Params: Figures
        self.figSize = (9.5, 8) # (width, height)
        self.figSizeWide = (9.5, 5)
        self.labelSizeTitle = 20 # Set fontsize
        self.labelSizeAxis = 18 # Set fontsize
        self.labelSizeTicks = 16 # Set fontsize
        self.labelSizeEM = 11  # Set fontsize
        self.lineThickness = 1.5
        self.tickLength = 4
        self.figureResolution = 600


    def plotLines(self, data):
        
        fig, ax = plt.subplots(figsize=self.figSize))
        ax.plot(time, y, color='#101010', linewidth=self.lineThickness, label=label)
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

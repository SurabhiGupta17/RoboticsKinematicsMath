import matplotlib.pyplot as plt
import numpy as np

from matplotlib.backend_bases import MouseButton
from matplotlib.transforms import Affine2D
import mpl_toolkits.axisartist.floating_axes as floating_axes

fig, ax1 = plt.subplots()
ax1.set_xlim(0, 50)
ax1.set_ylim(0, 50)
ax1.set_box_aspect(1)


# ax2.set_box_aspect(1)

counter = 0
scales = (0, 50, 0, 50)
t = Affine2D().rotate_deg(25)

# Add floating axes
h = floating_axes.GridHelperCurveLinear(t, scales)
ax2 = floating_axes.FloatingSubplot(fig, 111, grid_helper=h)

fig.add_subplot(ax2)

def on_click(event):
    global u, v, counter
    if event.button is MouseButton.LEFT:
        u = event.xdata
        v = event.ydata
        if counter < 1:
            ax1.quiver(0, 0, u, v, 
                       color = 'k', 
                       units = 'xy', 
                       scale = 1, 
                       headaxislength = 4, 
                       headlength = 4, 
                       headwidth = 4, 
                       width = 0.4)
            counter += 1
            ax1.text(u, v, f'({u:.2f}, {v:.2f})')
        plt.draw()
        

plt.connect('button_press_event', on_click)
plt.show()

# This script creates an interactive graphic, where the user can set a1 and a2 coeffitients by clicking a point in left graph. The right graph will show the corresponding impulse response of the defined system

import matplotlib
import numpy 
from matplotlib import pyplot

matplotlib.style.use('sv1_style.mplstyle')

def impulse(num_samples, a2, a1):
    '''
    calculates the impulse response of length 
    num_samples for the two recursive factors a1, and a2
    
    Parameters:
    -----------
    num_samples : int
        length of impulse response
    a2 : float
        recursive factor (2 sample delay)
    a1 : float
        recursive factor (1 sample delay)
    '''
    x = numpy.zeros(num_samples)
    x[0] = 1.
    y = numpy.zeros(num_samples)
    for idx in range(num_samples):
        y[idx] = x[idx] - a1*y[idx-1] - a2*y[idx-2]
    return y
    
def onclick(event):
    '''
    on click the mark is set in the stability triangle and the 
    resulting impulse response is calculated and displayed
    
    Parameters:
    -----------
    event : Event
        Event containing information about the click
    '''
    # read axis values of click as a1 and a2 factor
    a1 = event.ydata
    a2 = event.xdata
    ax_stab.lines[0].set_data(a2, a1)
    y = impulse(num_samples, a2, a1)
    ax_impuls.cla()
    ax_impuls.stem(y, use_line_collection=True)
    ax_impuls.set(xlabel='Folgenkindex k ->', ylabel='Amplitude', 
            title=f'Impulsantwort des Systems y[k] = \
            x[k] - {a1:.3f}*y[k-1] - {a2:.3f}*y[k-2]', 
            xlim=[0, num_samples-1], ylim=[-y.max(), y.max()])
    pyplot.draw()
    fig.canvas.draw_idle()

# creates the triangle area in which the system is stable
edges = numpy.array([[-1, 0],[1, -2],[1, 2]])
triangle = pyplot.Polygon(edges[:], color='grey')

# coefficient values
a1 = 0.0
a2 = 0.0

fig, (ax_stab, ax_impuls) = pyplot.subplots(1, 2)

# Stability Plot
ax_stab.add_patch(triangle)
ax_stab.set(xlabel='a2', ylabel='a1', title='stabilitätsdreieck', 
        xlim=[-2, 2], ylim=[-3, 3])
ax_stab.plot(a2, a1, 'X')

# Impulse Plot
num_samples = 50
y = impulse(num_samples, a1, a2)
ax_impuls.stem(y, use_line_collection=True)
ax_impuls.set(xlabel='Folgenkindex k ->', ylabel='Amplitude', 
        title=f'Impulsantwort des Systems y[k] = \
        x[k] - {a1:.3f}*y[k-1] - {a2:.3f}*y[k-2]', 
        xlim=[0, num_samples-1])

# Execute onclick when button is pressed
cid = fig.canvas.mpl_connect('button_press_event', onclick)

pyplot.show()
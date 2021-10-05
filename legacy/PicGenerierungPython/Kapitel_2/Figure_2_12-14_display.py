import matplotlib
import numpy
from matplotlib import pyplot
from matplotlib.widgets import Slider

matplotlib.style.use('sv1_style.mplstyle')

# adapted from: https://matplotlib.org/3.1.3/gallery/widgets/slider_demo.html

amplitude = 1.5
freq = 10 # in Hz
delta_f = 1 # in Hz
phase = numpy.pi/4 # in rad
T = 0.02 # Time in s
t = numpy.linspace(0, 0.3, 300) # 0 to 0.02 s

# calculates sinus with given values
sin_t = amplitude * numpy.sin(2 * numpy.pi * t * freq + phase)

# plots sinus
fig_sin, ax_sin = pyplot.subplots()
graph, = ax_sin.plot(t, sin_t, lw=1) # current graph
# used as previous graph to compare with current
graph_prev, = ax_sin.plot(t, sin_t, lw=0.5, ls=':') 
ax_sin.set(xlabel='Zeit is s', ylabel='Amplitude', 
        title=f'{amplitude}*sin(2π*{freq} + {phase/numpy.pi}π)', 
        xlim=[0, 0.3], ylim=[-2, 2])

pyplot.show()
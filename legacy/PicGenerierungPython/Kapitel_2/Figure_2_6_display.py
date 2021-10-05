import matplotlib
import numpy
from matplotlib import pyplot
from matplotlib.widgets import Slider
from matplotlib.widgets import RadioButtons

matplotlib.style.use('sv1_style.mplstyle')

#'continous' sample is sampled as such a high frequency that it seem continuous
fs_cont = 100000 
fs = 1000 # discrete sampled
freq = 200 # sinus frequency in Hz
steps = int(fs_cont/fs) # number of 'continuous' steps between discrete steps
T = 0.02 # signal length in s

# time vectors
t = numpy.linspace(0, T, int(T*fs_cont+1)) # 'continuous'
dt = t[0:len(t):steps] # extracts discrete time from continuous time

# function values
sin_t = numpy.sin(2 * numpy.pi * t * freq) # continuous
sin_dt = numpy.sin(2 * numpy.pi * dt * freq) # discrete

# plots
fig_sin, ax_sin = pyplot.subplots()
graph, = ax_sin.plot(t, sin_t)
markerline, stemlines, baseline = ax_sin.stem(
        dt, sin_dt, use_line_collection=True)

ax_sin.set_xlim([0, 0.02])
ax_sin.set(ylabel='Amplitude', xlabel='Zeit in s')
ax_sin.set_title(f'Sinus = {freq} Hz, Abtastfrequenz = 1000 Hz')

pyplot.show()
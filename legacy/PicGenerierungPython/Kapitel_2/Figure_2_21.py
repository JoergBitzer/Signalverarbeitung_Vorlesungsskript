import matplotlib
import numpy
from matplotlib import pyplot

matplotlib.style.use('sv1_style.mplstyle')

fs = 2000 #in Hz
duration = 0.01 #in s
time = numpy.linspace(0, duration, round(duration*fs)+1)
signal = []
tau = 0.003 #in s
for idx in range(len(time)):
    signal.append(numpy.exp(-1/tau*time[idx]))

time_ms = time * 1000 # simple conversion for better plotting
fig_delta, ax_delta = pyplot.subplots()
ax_delta.stem(time_ms, signal)
ax_delta.set(xlabel='Folgenkindex k ->', ylabel='Amplitude x(k)', 
        title='Exponentialimpuls mit tau = 0.3 ms und fs = 2000 Hz', 
        xlim=[0, 10])

pyplot.show()
import matplotlib
import numpy
from matplotlib import pyplot

matplotlib.style.use('sv1_style.mplstyle')

fs = 10000
duration = 1 # in s
time = numpy.linspace(0, duration, round(duration*fs) + 1)
signal = []
tau = 0.3 # in 1/s
for idx in range(len(time)):
    signal.append(numpy.exp(-1/tau*time[idx]))

fig_delta, ax_delta = pyplot.subplots()
ax_delta.plot(time, signal)
ax_delta.set(xlabel='Zeit is s', ylabel='Amplitude',
        title='Exponentialimpuls mit tau=0.3 s', xlim=[0, 1], ylim=[-1, 1])

pyplot.show()
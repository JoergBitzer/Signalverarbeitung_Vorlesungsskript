import matplotlib
import numpy
from matplotlib import pyplot

matplotlib.style.use('sv1_style.mplstyle')


f0 = 250
dauer = 0.01
n = 1000

time = numpy.linspace(0, dauer, 1000)
dt = dauer/n
d_phase = 2*numpy.pi*dt*f0

cur_phase = 0
signal = [0]*len(time)

for idx in range(len(time)):
    if (cur_phase<numpy.pi):
        signal[idx] = 1 - cur_phase/(0.5*numpy.pi)
    else:
        signal[idx] = -3 + cur_phase/(0.5*numpy.pi)
    cur_phase += d_phase
    if (cur_phase >= 2*numpy.pi):
        cur_phase -= 2*numpy.pi
    

fig_delta, ax_delta = pyplot.subplots()
ax_delta.plot(time, signal)
ax_delta.set(xlabel='Zeit in s', ylabel='Amplitude', title='Dreieck-Signal 250 Hz', xlim=[0, 0.01], ylim=[-1, 1])


pyplot.show()




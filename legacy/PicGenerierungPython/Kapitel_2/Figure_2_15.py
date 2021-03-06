import matplotlib
import numpy
from matplotlib import pyplot

matplotlib.style.use('sv1_style.mplstyle')


f0 = 250 # base frequency
duration = 0.01 # in s
fs = 40000 
num_samples = int(numpy.round(fs*duration))

dt = duration/num_samples
d_phase = 2*numpy.pi*dt*f0


time = numpy.linspace(0, duration, num_samples)


cur_phase = 0
signal = []


for idx in range(len(time)):
    # calculates values depending of phase, with line
    if (cur_phase<numpy.pi):
        val = 1 - cur_phase/(0.5*numpy.pi)
    else:
        val = -3 + cur_phase/(0.5*numpy.pi)
    signal.append(val)
    #update phase with values around 0 -> 2*pi
    cur_phase += d_phase
    if (cur_phase >= 2*numpy.pi):
        cur_phase -= 2*numpy.pi
    

fig_delta, ax_delta = pyplot.subplots()
ax_delta.plot(time, signal)
ax_delta.set(xlabel='Zeit in s', ylabel='Amplitude', 
        title='Dreieck-Signal 250 Hz', xlim=[0, 0.01], ylim=[-1, 1])


pyplot.show()




import matplotlib
import numpy
from matplotlib import pyplot

matplotlib.style.use('sv1_style.mplstyle')


f0 = 250
dur = 0.01
fs = 10000

time = numpy.linspace(0, dauer, numpy.round(fs*dur))
dt = dur/n
d_phase = 2*numpy.pi*dt*f0

cur_phase = 0
signal = [0]*len(time)

for idx in range(len(time)):
    if (cur_phase<numpy.pi):
        signal[idx] = 1
    else:
        signal[idx] = -1
        
    cur_phase += d_phase
    if (cur_phase >= 2*numpy.pi):
        cur_phase -= 2*numpy.pi
    

fig_delta, ax_delta = pyplot.subplots()
ax_delta.plot(time, signal)
ax_delta.set(xlabel='Zeit in s', ylabel='Amplitude', title='Rechteck-Signal 250 Hz', xlim=[0, 0.01], ylim=[-1, 1])
pyplot.show()




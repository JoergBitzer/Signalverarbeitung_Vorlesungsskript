import matplotlib
import numpy
from matplotlib import pyplot

matplotlib.style.use('sv1_style.mplstyle')


time = numpy.linspace(-12, 12, 241)
sinc = [0]*len(time)

fs = 1000
f0 = 5

for idx in range(len(time)):
    if (time[idx]!=0):
        sinc[idx] = numpy.sin(f0* time[idx])/(f0 * time[idx])
    else:
        sinc[idx] = 1

fig_delta, ax_delta = pyplot.subplots()
ax_delta.plot(time, sinc)
ax_delta.set(xlabel='Zeit in s', ylabel='Amplitude', title='si-Funktion', xlim=[-12, 12])

pyplot.show()
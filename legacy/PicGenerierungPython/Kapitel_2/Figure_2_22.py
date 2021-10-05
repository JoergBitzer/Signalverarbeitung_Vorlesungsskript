import matplotlib
import numpy
from matplotlib import pyplot

matplotlib.style.use('sv1_style.mplstyle')

spread = 12
time = numpy.linspace(-spread, spread, 20*spread+1)
sinc = []

fs = 1000 # sampling frequency
f0 = 5 # Sinc frequency

for idx in range(len(time)):
    if (time[idx]!=0):
        sinc.append(numpy.sin(f0* time[idx])/(f0 * time[idx]))
    else:
        sinc.append(1)

fig_delta, ax_delta = pyplot.subplots()
ax_delta.plot(time, sinc)
ax_delta.set(xlabel='Zeit in s', ylabel='Amplitude', 
        title='si-Funktion', xlim=[-12, 12])

pyplot.show()
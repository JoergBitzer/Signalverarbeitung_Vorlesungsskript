import matplotlib
import numpy
from matplotlib import pyplot

matplotlib.style.use('sv1_style.mplstyle')

samples = numpy.linspace(-15, 15, 31)
si = [0]*len(samples)

fs = 1000 # sampling frequency
f0 = 100 # Si-frequency

# Berechnet Werte
for val in samples:
    if (val!=0):
        si.append(numpy.sin(2*numpy.pi * f0 * val/fs )/(2*numpy.pi*val*f0/fs))
    else:
        # at 0 si is 1 to avoid division by zero
        si.append(1)
        
fig_delta, ax_delta = pyplot.subplots()
ax_delta.stem(samples, si)
ax_delta.set(xlabel='Folgenkindex k ->', ylabel='Amplitude x(k)', 
        title='Diskrete SI-Funktion', xlim=[-15, 15])

pyplot.show()
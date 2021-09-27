import matplotlib
import numpy
from matplotlib import pyplot

matplotlib.style.use('sv1_style.mplstyle')

# sample und funktionsvektor
samples = numpy.linspace(-15, 15, 31)
si = [0]*len(samples)
#mid = int(numpy.floor(len(samples)/2))

fs = 1000 # Sampling Frequenz
f0 = 100 # Si-Frequenz

# Berechnet Werte
for idx in range(len(samples)):
    if (samples[idx]!=0):
        si[idx] = numpy.sin(2*numpy.pi * f0 * samples[idx]/fs )/(2*numpy.pi*samples[idx]*f0/fs)
    # in der Mitte ist si-Funktion = 1, da sonst durch Null geteilt wird
    else:
        si[idx] = 1
        
fig_delta, ax_delta = pyplot.subplots()
ax_delta.stem(samples, si)
ax_delta.set(xlabel='Folgenkindex k ->', ylabel='Amplitude x(k)', title='Diskrete SI-Funktion', xlim=[-15, 15])

pyplot.show()
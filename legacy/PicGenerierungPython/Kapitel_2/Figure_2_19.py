import matplotlib
import numpy
from matplotlib import pyplot

matplotlib.style.use('sv1_style.mplstyle')

idx = numpy.linspace(-6, 6, 13)
amplitude = [0]*len(idx)
mid = int(numpy.floor(len(idx)/2))
amplitude[mid:] = numpy.ones(len(amplitude)-mid)

fig_delta, ax_delta = pyplot.subplots()
ax_delta.stem(idx, amplitude)
ax_delta.set(xlabel='Folgenkindex k ->', ylabel='Amplitude x(k)', title='Sprungfunktion')
ax_delta.set_xlim([-6, 6])

pyplot.show()
import matplotlib
import numpy
from matplotlib import pyplot

matplotlib.style.use('sv1_style.mplstyle')

ax_signal = pyplot.subplot(3, 1, 1)
signal = numpy.random.random_sample(36)*4 - 2
ax_signal.stem(range(36), signal, use_line_collection=True)
ax_signal.set(xlabel='Folgenkindex k ->', ylabel='Amplitude x[k]', title='Eingangssignal', xlim=[0, 35])

ax_window = pyplot.subplot(3, 1, 2)
window = numpy.concatenate([[0]*10, [1]*16, [0]*10])
ax_window.step(range(36), window, where='mid')
ax_window.set(xlabel='Folgenkindex k ->', ylabel='Amplitude x[k]', title='Rechteck-Fensterfunktion', xlim=[0, 35])

ax_filtered = pyplot.subplot(3, 1, 3)
filtered_signal = signal * window
ax_filtered.stem(range(36), filtered_signal, use_line_collection=True)
ax_filtered.set(xlabel='Folgenkindex k ->', ylabel='Amplitude x[k]', title='gefenstertes Signal', xlim=[0, 35])

pyplot.show()
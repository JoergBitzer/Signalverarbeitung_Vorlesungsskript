import matplotlib
import numpy
from matplotlib import pyplot

# determine where we're running from and set paths accordingly
try: 
    if get_ipython().__class__.__name__ == 'ZMQInteractiveShell':
        prefix = ''
except:
    prefix = '../../'

matplotlib.style.use(f'{prefix}sv.mplstyle')

samples = numpy.linspace(-15, 15, 31)
fs = 1000 # sampling frequency
f0 = 100 # Si-frequency

# Berechnet Werte
si = []
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

# glue this figure to paste it later (no effect outside of MyST NB)
from myst_nb import glue
glue("SiFunktionDiskret", fig_delta, display=False)
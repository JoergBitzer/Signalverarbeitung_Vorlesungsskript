# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Demoscript for "Signalverarbeitung 1"
#
# Version: 1.0   17.02.2022
# 
# This software is released as public domain under CC0 1.0
# https://creativecommons.org/publicdomain/zero/1.0/
#-------------------------------------------------------------------------------

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

idx = numpy.linspace(-6, 6, 13)
amplitude = [0]*len(idx)
mid = int(numpy.floor(len(idx)/2))
# ones from mid onward means from 0 onward in the plot
amplitude[mid:] = numpy.ones(len(amplitude)-mid)

fig_delta, ax_delta = pyplot.subplots()
ax_delta.stem(idx, amplitude)
ax_delta.set(xlabel='Folgenkindex k ->', ylabel='Amplitude x(k)', 
        title='Sprungfunktion')
ax_delta.set_xlim([-6, 6])

pyplot.show()

# glue this figure to paste it later (no effect outside of MyST NB)
from myst_nb import glue
glue("Sprungfolge", fig_delta, display=False)

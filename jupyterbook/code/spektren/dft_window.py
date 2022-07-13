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
import matplotlib.pyplot as pyplot

# determine where we're running from and set paths accordingly
try: 
    if get_ipython().__class__.__name__ == 'ZMQInteractiveShell':
        prefix = ''
except:
    prefix = '../../'

matplotlib.style.use(f'{prefix}sv.mplstyle')

fig, ax = pyplot.subplots(nrows=3, ncols=1)
ax_signal = ax[0]
signal = numpy.random.random_sample(36)*4 - 2 # random sample scaled -2 to 2
ax_signal.stem(range(-10,26), signal, use_line_collection=True)
ax_signal.set(xlabel='Folgenkindex k ->', ylabel='Amplitude x[k]', 
        title='Eingangssignal', xlim=[-10, 26])

ax_window = ax[1]
window = numpy.concatenate([[0]*10, [1]*16, [0]*10])
ax_window.step(range(-10,26), window, where='mid')
ax_window.set(xlabel='Folgenkindex k ->', ylabel='Amplitude x[k]', 
        title='Rechteck-Fensterfunktion', xlim=[-10, 26])

ax_filtered = ax[2]
filtered_signal = signal * window # filtering in time domain
ax_filtered.stem(range(-10,26), filtered_signal, use_line_collection=True)
ax_filtered.set(xlabel='Folgenkindex k ->', ylabel='Amplitude x[k]', 
        title='gefenstertes Signal', xlim=[-10, 26])

pyplot.tight_layout()

pyplot.show()

# glue this figure to paste it later (no effect outside of MyST NB)
from myst_nb import glue
glue("DFT_FensterMultiplikation", fig, display=False)
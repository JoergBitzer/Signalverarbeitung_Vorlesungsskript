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

fs = 2000 #in Hz
duration = 0.01 #in s
time = numpy.linspace(0, duration, round(duration*fs)+1)
signal = []
tau = 0.003 #in s
for idx in range(len(time)):
    signal.append(numpy.exp(-1/tau*time[idx]))

time_ms = time * 1000 # simple conversion for better plotting
fig_delta, ax_delta = pyplot.subplots()
ax_delta.stem(time_ms, signal)
ax_delta.set(xlabel='Folgenkindex k ->', ylabel='Amplitude x(k)', 
        title='Exponentialimpuls mit tau = 0.3 ms und fs = 2000 Hz', 
        xlim=[0, 10])

pyplot.show()

# glue this figure to paste it later (no effect outside of MyST NB)
from myst_nb import glue
glue("ExpImpulseDiskret", fig_delta, display=False)
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

fs = 10000
duration = 1 # in s
time = numpy.linspace(0, duration, round(duration*fs) + 1)
signal = []
tau = 0.3 # in 1/s
for idx in range(len(time)):
    signal.append(numpy.exp(-1/tau*time[idx]))

fig_delta, ax_delta = pyplot.subplots()
ax_delta.plot(time, signal)
ax_delta.set(xlabel='Zeit is s', ylabel='Amplitude',
        title='Exponentialimpuls mit tau=0.3 s', xlim=[0, 1])

pyplot.show()

# glue this figure to paste it later (no effect outside of MyST NB)
from myst_nb import glue
glue("ExpImpulse", fig_delta, display=False)
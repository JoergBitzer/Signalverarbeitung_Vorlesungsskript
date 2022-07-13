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

# glue this figure to paste it later (no effect outside of MyST NB)
from myst_nb import glue
glue("SIFunktion", fig_delta, display=False)
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

f0 = 250
duration = 0.01
fs = 10000
num_samples = int(numpy.round(fs*duration))
time = numpy.linspace(0, duration, num_samples)
dt = 1/fs
d_phase = 2*numpy.pi*f0*dt

cur_phase = 0
signal = []

for idx in range(len(time)):
    if (cur_phase<numpy.pi):
        val = 1
    else:
        val = -1
    signal.append(val)
    #update phase with values around 0 -> 2*pi
    cur_phase += d_phase
    if (cur_phase >= 2*numpy.pi):
        cur_phase -= 2*numpy.pi

    

fig_delta, ax_delta = pyplot.subplots()
ax_delta.plot(time, signal)
ax_delta.set(xlabel='Zeit in s', ylabel='Amplitude', 
        title='Rechteck-Signal 250 Hz', xlim=[0, 0.01], ylim=[-1.1, 1.1])

pyplot.show()

# glue this figure to paste it later (no effect outside of MyST NB)
from myst_nb import glue
glue("Rechteck", fig_delta, display=False)

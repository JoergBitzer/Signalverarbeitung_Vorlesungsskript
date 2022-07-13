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
from matplotlib.widgets import Slider

# determine where we're running from and set paths accordingly
try: 
    if get_ipython().__class__.__name__ == 'ZMQInteractiveShell':
        prefix = ''
except:
    prefix = '../../'

matplotlib.style.use(f'{prefix}sv.mplstyle')

# adapted from: https://matplotlib.org/3.1.3/gallery/widgets/slider_demo.html

amplitude = 1.5
freq = 10 # in Hz
delta_f = 1 # in Hz
phase = numpy.pi/4 # in rad
T = 0.02 # Time in s
t = numpy.linspace(0, 0.3, 300) # 0 to 0.02 s

# calculates sinus with given values
sin_t = amplitude * numpy.sin(2 * numpy.pi * t * freq + phase)

# plots sinus
fig_sin, ((ax_ampl, ax_freq), (ax_phase, ax_empty)) = pyplot.subplots(2, 2)
ax_ampl.plot(t, sin_t, lw=1)
ax_ampl.plot(t, 0.5*sin_t, lw=1, ls=':')
ax_freq.plot(t, sin_t, lw=1)
ax_freq.plot(t, amplitude * numpy.sin(2 * numpy.pi * t * 0.6*freq + phase), ls=':')
ax_phase.plot(t, sin_t, lw=1)
ax_phase.plot(t, amplitude * numpy.sin(2 * numpy.pi * t * freq + phase*2), ls=':')
          
ax_ampl.set(xlabel='Zeit is s', ylabel='Amplitude', 
        title=f'{amplitude} -> {0.5*amplitude} Amplitude', 
        xlim=[0, 0.3], ylim=[-2, 2])
ax_freq.set(xlabel='Zeit is s', ylabel='Amplitude', 
        title=f'{freq} -> {0.6*freq} Hz Frequency', 
        xlim=[0, 0.3], ylim=[-2, 2])
ax_phase.set(xlabel='Zeit is s', ylabel='Amplitude', 
        title=f'{phase/numpy.pi}π -> {2*phase/numpy.pi}π Phase', 
        xlim=[0, 0.3], ylim=[-2, 2])
pyplot.tight_layout()

pyplot.show()

# glue this figure to paste it later (no effect outside of MyST NB)
from myst_nb import glue
glue("Sinewave", fig_sin, display=False)
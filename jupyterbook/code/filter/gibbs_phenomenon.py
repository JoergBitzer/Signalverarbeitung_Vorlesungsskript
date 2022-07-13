# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Demoscript for "Signalverarbeitung 1"
#
# Version: 1.0   18.02.2022
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

fig, (ax_si, ax_spec) = pyplot.subplots(1,2)

samples = numpy.linspace(-100, 100, 201)
si = [0]*len(samples)
mid = int(numpy.floor(len(samples)/2))

fs = 1000
f0 = 100

for idx in range(len(samples)):
    if (samples[idx]!=0):
        si[idx] = numpy.sin(2*numpy.pi * f0 * samples[idx]/fs)/(2*numpy.pi*samples[idx]*f0/fs)
    else:
        # si(0) = 1 to avoid division by zero
        si[idx] = 1

# cut si-function
si_short = si[(mid-25):(mid+25)]
samples_short = samples[(mid-25):(mid+25)]

#ax_si = pyplot.subplot(1, 2, 1)
ax_si.plot(samples, si, linestyle='dotted')
ax_si.plot(samples_short, si_short)
ax_si.set(xlabel='Folgenkindex k ->', ylabel='Amplitude x(k)', 
        title='SI-Funktion')
ax_si.set_xlim([-100, 100])

# zero padding, for display resolution
si_short = [0]*100 + si_short + [0]*100
si = [0]*100 + si + [0]*100

spectrum_short = numpy.fft.fft(si_short)
spectrum = numpy.fft.fft(si)

w = numpy.linspace(0, 2, len(si))
w_short = numpy.linspace(0, 2, len(si_short))

#ax_spec = pyplot.subplot(1, 2, 2)
ax_spec.plot(w_short, 20 * numpy.log10(abs(spectrum_short)), 
        linestyle='dotted')
ax_spec.plot(w, 20 * numpy.log10(abs(spectrum))) # dB spectrum
ax_spec.set(xlabel='Frequenz normalisiert mit w/pi', ylabel='Amplitude in dB', 
        title='Spektrum', xlim=([0, 0.4]))

pyplot.show()

# glue this figure to paste it later (no effect outside of MyST NB)
from myst_nb import glue
glue("GippsPheanomen", fig, display=False)
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

# create a rectengular window
rect_window = numpy.concatenate([[0]+[1]*30+[0]])
# and do zero padding
rect_window = numpy.concatenate([rect_window, [0]*1000])

spectrum = numpy.fft.fft(rect_window)
mid = numpy.floor(len(spectrum)/2)
# shift area from pi -> 2pi to -pi -> 0
spectrum = numpy.concatenate([spectrum[int(mid):], spectrum[:int(mid)]]) 
# dB maximum = 0dB
spectrum_abs = 20*numpy.log10(numpy.abs(spectrum)/numpy.abs(spectrum).max()) 
freqs_fft = numpy.linspace(-1, 1, len(spectrum_abs)) # freq bins, for plotting

fig, (ax_sample, ax_spectrum) = pyplot.subplots(1, 2)
ax_sample.plot(rect_window)
ax_sample.set(xlabel='Folgenndex k ->', ylabel='Amplitude x[k]', 
        xlim=[0, 31], title='Rechteck-Fenster im Frequenzbereich')

ax_spectrum.plot(freqs_fft, spectrum_abs)
ax_spectrum.set(xlabel='Frequenz rad/pi ', ylabel='Dämpfung in dB', 
        title='Rechteck-Fenster im Frequenzbereich')

pyplot.show()

# glue this figure to paste it later (no effect outside of MyST NB)
from myst_nb import glue
glue("RechteckWindow", fig, display=False)
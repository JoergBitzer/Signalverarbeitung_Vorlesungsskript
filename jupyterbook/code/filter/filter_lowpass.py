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
import scipy
from scipy import signal
from matplotlib import pyplot

# Script to create an ideal and realistic lowpass

# determine where we're running from and set paths accordingly
try: 
    if get_ipython().__class__.__name__ == 'ZMQInteractiveShell':
        prefix = ''
except:
    prefix = '../../'

matplotlib.style.use(f'{prefix}sv.mplstyle')

Fs = 8000
fg = 1000 # cutoff frequency
order = 6
x = [0.0]*Fs
x[0] = 1.0
b, a = scipy.signal.butter(N=order, Wn=fg, btype='low', output='ba', fs=Fs)
y = scipy.signal.lfilter(b, a, x)
spectrum = numpy.fft.fft(y)

# dB, max amplitude = 0dB
spectrum_abs = 20*numpy.log10(numpy.abs(spectrum)/numpy.abs(spectrum).max()) 
freq_vec = numpy.linspace(0, Fs, len(spectrum_abs)) # freq bins, for plotting

fig, ax_spectrum = pyplot.subplots()

# ideal frequency respose of filter
ax_spectrum.step(y=[0, 0, -100, - 100, 0], x=[0, fg, Fs/2, Fs-fg, Fs], 
        color='r', label="Optimale Entwurfsvorgabe")
# actual realization
ax_spectrum.plot(freq_vec, spectrum_abs, color='b', 
        label="Mögliche Realisierung")

ax_spectrum.set(xlabel='Frequenz in Hz ', ylabel='Dämpfung in dB', 
        xlim=[0, Fs/2], ylim=[-105, 5], title=f'Tiefpass {order}.Odnung')
pyplot.legend()

pyplot.show()

# glue this figure to paste it later (no effect outside of MyST NB)
from myst_nb import glue
glue("DesignTP", fig, display=False)
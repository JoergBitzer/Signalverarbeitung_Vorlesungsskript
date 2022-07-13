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
from scipy import signal
from matplotlib import pyplot

# determine where we're running from and set paths accordingly
try: 
    if get_ipython().__class__.__name__ == 'ZMQInteractiveShell':
        prefix = ''
except:
    prefix = '../../'

matplotlib.style.use(f'{prefix}sv.mplstyle')

eps = numpy.finfo(float).eps # for slight offset to avoid division by 0

# create exemplary non-recursive filter coefficients (mirrored at unit circle)
b1 = [0.98]*4
b2 = [1.0/0.98]*4
h = numpy.poly(numpy.concatenate((b1, b2)))
h = [0.5, 0.7, 0.9, 1.1, 2, 1.1, 0.9, 0.7, 0.5]
h = numpy.array(h)/numpy.sum(h)
W, H = signal.freqz(b=h, a=1, worN=4*1024, whole=True)
fig, ((ax_H, ax_void), (ax_lin_zeit, ax_min_zeit), 
        (ax_lin_phase, ax_min_phase)) = pyplot.subplots(3, 2)

# create a linear phase filter from the exististing impulse response
log_H = numpy.log(numpy.abs(H)+eps)
h_c = numpy.fft.ifft(log_H).real
h_c[1 : int(len(h_c)/2)] *= 2
h_c[int(len(h_c)/2)+1 : ] = 0 
H_min_log = numpy.fft.fft(h_c)
H_min = numpy.exp(H_min_log)
h_min = numpy.fft.ifft(H_min)
h_min = h_min[0:8]

ax_H.plot(W, 20*numpy.log10(numpy.abs(H)+eps))
ax_lin_zeit.stem(h, use_line_collection=True)
ax_min_zeit.stem(h_min, use_line_collection=True)
ax_lin_phase.plot(numpy.unwrap(p=numpy.angle(H)))
ax_min_phase.plot(numpy.unwrap(p=numpy.angle(H_min)))

pyplot.show()

# glue this figure to paste it later (no effect outside of MyST NB)
from myst_nb import glue
glue("MinPhasenBsp", fig, display=False)
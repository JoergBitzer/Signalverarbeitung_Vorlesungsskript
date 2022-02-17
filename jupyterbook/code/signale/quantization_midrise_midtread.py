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

bits = 2 # number of bits used to quantize, feel free to change this

# calculating the vectors to plot 
input_midrise = numpy.linspace(-1 + (1/2**(bits-1)), 1, 2**bits)
output_midrise = numpy.linspace(-1 + 2**-bits, 1 - (1/2**bits), 2**bits)

input_midtread = numpy.linspace(-1 + (1/2**bits), 1 - (1/2**bits), 2**bits)
output_midtread = numpy.linspace(-1, 1 - (1/2**(bits-1)), 2**bits)

# appending  limiting values to the edges of the vector,
# this is purely for displaying purposes, to avoid a misleading
# end of quantization after the last calculated values
input_midrise = numpy.concatenate([[-2], input_midrise, [2]])
input_midtread = numpy.concatenate([[-2], input_midtread, [2]])
output_midrise = numpy.concatenate(
        [[-1 + 2**-bits], output_midrise, [1 - (1/2**bits)]])
output_midtread = numpy.concatenate(
        [[-1], output_midtread, [1 - (1/2**(bits-1))]])

fig, (ax_rise, ax_tread) = pyplot.subplots(1, 2)
# plots the quantizer lines as step diagrams

ax_rise.step(input_midrise, output_midrise, where='pre', linewidth=2)
ax_rise.plot([-2, 2], [-2, 2], 'o--', color='blue', alpha=0.5, linewidth=2)
ax_rise.set(xlabel='input', ylabel='output', title='Mid-Rise Quantisierer', 
        xlim=[-2, 2], ylim=[-1, 1])

ax_tread.step(input_midtread, output_midtread, where='pre', linewidth=2)
ax_tread.plot([-2, 2], [-2, 2], 'o--', color='blue', alpha=0.5, linewidth=2)
ax_tread.set(xlabel='input', ylabel='output', title='Mid-Tread Quantisierer', 
        xlim=[-2, 2], ylim=[-1, 1])

pyplot.show()

# glue this figure to paste it later (no effect outside of MyST NB)
from myst_nb import glue
glue("MidRiseMidTread", fig, display=False)
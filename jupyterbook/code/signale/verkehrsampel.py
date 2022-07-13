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
from matplotlib.widgets import RadioButtons

# determine where we're running from and set paths accordingly
try: 
    if get_ipython().__class__.__name__ == 'ZMQInteractiveShell':
        prefix = ''
except:
    prefix = '../../'

matplotlib.style.use(f'{prefix}sv.mplstyle')

d_t = 5 # timespan of one datapoint

# first 4 datapoints set the order of the colours on the axis
# and are not valid data points
lights = ["green", "yellow", "yellow/red", "red", "red", "red", 
        "red", "yellow/red", "green", "green", "green", "yellow", "red", "red", "red"] 
t = numpy.linspace(0, d_t*(len(lights)-1), len(lights))

fig, ax = pyplot.subplots()
line, = ax.step(t, lights, where='post') # defines the steps of a step diagram
ax.grid(axis='x', color='0.8')
ax.set(xlabel='Zeit in s', ylabel='Ampelfarbe')
ax.set_xlim((15, 70))

pyplot.show()

# glue this figure to paste it later (no effect outside of MyST NB)
from myst_nb import glue
glue("verkehrsampel", fig, display=False)

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

N = 16 # filter length
freqs = numpy.linspace(-3, 3, 600) # frequency vector
dirichlet = [0]*len(freqs) 
for idx in range(len(freqs)):
    # calculate dirichlet function with sin(N*w/4)/sin(w/4)
    dirichlet[idx] = numpy.sin(N*freqs[idx]*numpy.pi*0.5)/ \
            numpy.sin(freqs[idx]*numpy.pi*0.5)

# normalizing
dirichlet_abs = numpy.abs(dirichlet)/numpy.abs(dirichlet).max()

fig, ax_dirichlet = pyplot.subplots()
ax_dirichlet.plot(freqs, dirichlet_abs)
ax_dirichlet.set(xlabel='Frequenz rad/pi ', 
        ylabel='Frequenzanteil normiert auf 1', 
        title='Spektrum eines Rechteckfenster (Dirichlet-Funktion)')

pyplot.show()

# glue this figure to paste it later (no effect outside of MyST NB)
from myst_nb import glue
glue("DirichletFkt", fig, display=False)
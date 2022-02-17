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

num_samples = 16
f0 = 155
fs = 1000

sample = [0]*num_samples

kk = numpy.arange(num_samples)
cos_series = numpy.cos(2*numpy.pi*f0*kk/fs)

sample = numpy.concatenate(([0]*4,cos_series,[0]*4))

reconst_sig = numpy.concatenate((cos_series[-4:],cos_series,cos_series[0:4]))


# signal reconstruction from fft through ifft
spectrum = numpy.fft.fft(sample,256)
spectrumshort = numpy.fft.fft(sample)

spectrumshort = numpy.fft.fftshift(numpy.abs(spectrumshort)/numpy.abs(spectrumshort).max())
spectrum = numpy.fft.fftshift(spectrum)
# dB normalized to 0 max amplitude
spectrum_abs = numpy.abs(spectrum)/numpy.abs(spectrum).max() 
# frequency bins for plotting
freqs_fft = numpy.linspace(-1, 1, len(spectrum_abs)) 
freqs_fftshort = numpy.linspace(-1, 1, len(spectrumshort)) 


fig, ax = pyplot.subplots(2, 2)
ax[0][0].stem(range(-4,len(sample)-4),sample)
ax[0][0].set(xlabel='Folgenndex k ->', ylabel='Amplitude x[k]', 
        title='Eingangssignal Sinus')

ax[0][1].plot(freqs_fft, spectrum_abs)
ax[0][1].set(xlabel='Frequenz rad/pi ', 
        ylabel='Frequenzanteil normiert auf 1', 
        title='Amplitudenspektrum der gefensterten Cosinus-Fkt')

ax[1][0].stem(freqs_fftshort, spectrumshort, use_line_collection=True)
ax[1][0].set(xlabel='Frequenz rad/pi ', 
        ylabel='Frequenzanteil normiert auf 1',
        title='Abgetastetes Amplitudenspektrum')

ax[1][1].stem(range(-4,len(sample)-4),reconst_sig)
ax[1][1].set(xlabel='Folgenndex k ->', ylabel='Amplitude x[k]', 
        title='durch Abtastung des Spektrums erzieltes rekonstruiertes Signal')
ax[1][1].plot([-0.5,-0.5],[-1,1], 'r:' )
ax[1][1].plot([15.5,15.5],[-1,1], 'r:')

pyplot.tight_layout()

pyplot.show()

# glue this figure to paste it later (no effect outside of MyST NB)
from myst_nb import glue
glue("DFT_Cosinus", fig, display=False)
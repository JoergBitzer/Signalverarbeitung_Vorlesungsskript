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
from matplotlib.widgets import Slider

# determine where we're running from and set paths accordingly
try: 
    if get_ipython().__class__.__name__ == 'ZMQInteractiveShell':
        prefix = ''
except:
    prefix = '../../'

matplotlib.style.use(f'{prefix}sv.mplstyle')

def get_peak_EQ(f_0, gain_dB, Q, f_s):
    '''
    calculates filter coefficients of a peak equalizer
    with the given parameters
    
    Parameters:
    -----------
    f_0 : int
        peak frequency in Hz
    gain_dB : int
        dB gain at peak
    Q : float
        Quality of filter
    f_s : int
        sampling frequency
    '''
    K = numpy.tan(2*numpy.pi*f_0/(f_s*2))
    a = [0]*3
    b = [0]*3
    den = 1
    if (gain_dB > 0):
        V0 = 10**(gain_dB/20)
        den = (1 + K/Q + K*K)
        b[0] = (1 + V0*K/Q + K*K)
        b[1] = 2 * (K*K - 1)
        b[2] = (1 - V0*K/Q + K*K)
        a[0] = 1
        a[1] = 2 * (K*K - 1)
        a[2] = (1 - K/Q + K*K)
    else:
        V0 = 10**(-gain_dB/20)
        den = (1 + V0*K/Q + K*K)
        b[0] = (1 + K/Q + K*K)
        b[1] = 2 * (K*K - 1)
        b[2] = (1 - K/Q + K*K)
        a[0] = 1
        a[1] = 2 * (K*K - 1)
        a[2] = (1 - V0*K/Q + K*K)
    
    b /= den
    a[1:] /= den
    
    return b, a
    

gains = [12, 6, 0, -6, -12]
fs = 48000
freq= 8000
Q = 3

fig, (ax_gain, ax_freq, ax_Q) = pyplot.subplots(3, 1)

for gain in gains:
    b, a = get_peak_EQ(freq, gain, Q, fs) # get filter coeefficients        
    w, h = signal.freqz(b, a, fs) # calculate impulse response
    h_db = 20*numpy.log10(numpy.abs(h)) # dB
    ax_gain.plot(w, h_db)

ax_gain.set(ylim=[-13, 13], xlabel='Frequenz in Hz', ylabel='Verstärkung in dB',     
        title=f'Peak-EQ mit variablem Gain \n\
        bei Frequenz f = {freq} Hz mit Güte Q = {Q:.1f}')

freqs = [0, fs/10, fs/5, fs/3]
gain = 12
for freq in freqs:
    b, a = get_peak_EQ(freq, gain, Q, fs) # get filter coeefficients
    w, h = signal.freqz(b, a, fs) # calculate impulse response
    h_db = 20*numpy.log10(numpy.abs(h)) # dB
    ax_freq.plot(w, h_db)
ax_freq.set(ylim=[-13, 13], xlabel='Frequenz in Hz', ylabel='Verstärkung in dB', 
        title=f'Peak-EQ mit variabler Frequenz \n\
        bei Gain = {gain} dB und Güte Q = {Q:.1f}')
Qs = [0, 1, 3, 10]
freq = 8000

for Q in Qs:
    b, a = get_peak_EQ(freq, gain, Q, fs) # get filter coeefficients
    w, h = signal.freqz(b, a, fs) # calculate impulse response
    h_db = 20*numpy.log10(numpy.abs(h)) # dB
    ax_Q.plot(w, h_db)
ax_Q.set(ylim=[-13, 13], xlabel='Frequenz in Hz', ylabel='Verstärkung in dB', 
         title=f'Peak-EQ mit variabler Güte \n\
         bei Frequenz f = {freq} Hz und Gain = {gain} dB')

pyplot.tight_layout()

pyplot.show()

# glue this figure to paste it later (no effect outside of MyST NB)
from myst_nb import glue
glue("EQ_GainParam", fig, display=False)
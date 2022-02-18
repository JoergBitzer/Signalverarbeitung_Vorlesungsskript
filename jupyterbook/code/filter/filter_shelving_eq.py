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
from matplotlib.widgets import RadioButtons
from matplotlib.widgets import Slider

# determine where we're running from and set paths accordingly
try: 
    if get_ipython().__class__.__name__ == 'ZMQInteractiveShell':
        prefix = ''
except:
    prefix = '../../'

matplotlib.style.use(f'{prefix}sv.mplstyle')

def getShelvingEQ(f_0, Gain_dB, shelf_type, fs):
    '''
    calculates filter coefficients of a shelving equalizer
    with the given parameters
    
    Parameters:
    -----------
    f_0 : int
        peak frequency in Hz
    gain_dB : int
        dB gain at peak
    shelf_type : str
        "high" for high-shelf, anything else for low shelf
    fs : int
        sampling frequency
    '''

    K = numpy.tan(2*numpy.pi*f_0/(fs*2))
    a = [0]*3
    b = [0]*3
    den = 1
    
    if (shelf_type == "high"): # High-Shelf
        if (Gain_dB > 0):
            V0 = 10**(Gain_dB/20)
            den = 1 + numpy.sqrt(2)*K + K*K
            b[0] = V0 + numpy.sqrt(2*V0)*K+K*K 
            b[1] = 2 * (K*K - V0) 
            b[2] = V0 - numpy.sqrt(2*V0)*K + K*K  
            a[0] = 1
            a[1] = 2 * (K*K - 1)            
            a[2] = 1 - numpy.sqrt(2)*K + K*K  
            b /= den
            a[1:] /= den
        else:
            V0 = 10**(-Gain_dB/20)
            den = V0 + numpy.sqrt(V0*2)*K + K*K
            b[0] = 1 + numpy.sqrt(2)*K + K*K 
            b[1] = 2 * (K*K - 1) 
            b[2] = 1 - numpy.sqrt(2)*K + K*K  
            b /= den
            den = 1 + numpy.sqrt(2/V0)*K + K*K/V0
            a[0] = 1
            a[1] = 2 * (K*K/V0 - 1) 
            a[2] = (1 - numpy.sqrt(2/V0)*K + K*K/V0)  
            a[1:] /= den
    else: #Low-Shelf 0 or default for != 1
        if (Gain_dB > 0):
            V0 = 10**(Gain_dB/20)
            den = 1 + numpy.sqrt(2)*K + K*K
            b[0] = 1 + numpy.sqrt(2*V0)*K + V0*K*K 
            b[1] = 2 * (V0*K*K - 1) 
            b[2] = 1 - numpy.sqrt(2*V0)*K + V0*K*K  
            a[0] = 1
            a[1] = 2 * (K*K - 1) 
            a[2] = 1 - numpy.sqrt(2)*K + K*K  
        else:
            V0 = 10**(-Gain_dB/20)
            den = 1 + numpy.sqrt(V0*2)*K + V0*K*K
            b[0] = 1 + numpy.sqrt(2)*K + K*K 
            b[1] = 2 * (K*K - 1) 
            b[2] = 1 - numpy.sqrt(2)*K + K*K  
            a[0] = 1
            a[1] = 2 * (V0*K*K - 1)
            a[2] = 1 - numpy.sqrt(V0*2)*K + V0*K*K
            
        b /= den
        a[1:] /= den

    return b, a

#parameters
gains = [12, 6, 0, -6, -12]
fs = 48000
f_c = 8000
shelf_types = ["low", "high"]

fig, (ax_gain, ax_freq) = pyplot.subplots(2, 1)

for gain in gains:
    for ftype in shelf_types:
        b, a = getShelvingEQ(f_c, gain, ftype, fs) # get filter coefficients
        print(b, a)
        w, h = signal.freqz(b, a, fs=fs) # calculate impulse response
        #with numpy.errstate(divide='ignore'):
        h_db = 20*numpy.log10(numpy.abs(h)) # dB
        ax_gain.plot(w, h_db)

ax_gain.set(ylim=[-13, 13], xlabel='Frequenz in Hz',ylabel='Verstärkung in dB', 
        title=f'Shelf-EQs variablem Gain \n bei Grenzfrequenz f = {f_c} Hz')

        

freqs = [0, fs/10, fs/5, fs/3]
gain = 12
for f_c in freqs:
    for ftype in shelf_types:
        b, a = getShelvingEQ(f_c, gain, ftype, fs) # get filter coefficients
        print(b, a)
        w, h = signal.freqz(b, a, fs = fs) # calculate impulse response
        with numpy.errstate(divide='ignore'):
            h_db = 20*numpy.log10(numpy.abs(h)) # dB
        ax_freq.plot(w, h_db)
ax_freq.set(ylim=[-13, 13], xlabel='Frequenz in Hz',ylabel='Verstärkung in dB', 
        title=f'Shelf-EQs mit variabler Grenzfrequenz \n bei Gain = {gain} dB')

pyplot.tight_layout()

pyplot.show()

# glue this figure to paste it later (no effect outside of MyST NB)
from myst_nb import glue
glue("EQ_ShelvParam", fig, display=False)
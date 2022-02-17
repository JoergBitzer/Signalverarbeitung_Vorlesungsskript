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
from scipy import signal
from matplotlib import pyplot
from matplotlib.widgets import RadioButtons
from matplotlib.widgets import Slider

matplotlib.style.use('sv1_style.mplstyle')

def getShelvingEQ(f_0, Gain_dB, shelf_type, f_s):
    '''
    calculates filter coefficients of a shelving equalizer
    with the given parameters
    
    Parameters:
    -----------
    f_0 : int
        peak frequency in Hz
    gain_dB : int
        dB gain at peak
    shelf_type : int
        1 for high-shelf, 0 (or anything else) for low shelf
    f_s : int
        sampling frequency
    '''

    K = numpy.tan(2*numpy.pi*f_0/(f_s*2))
    a = [0]*3
    b = [0]*3
    den = 1
    
    if (shelf_type == 1): # High-Shelf
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
gain = 12
f_s = 48000
f_c = 2000
shelf_type = 1

fig, ax_EQ = pyplot.subplots()
fig.subplots_adjust(left=0.3)

# adds a slider for cutoff frequency, gain and buttons for type of the EQ
axcolor = 'lightgoldenrodyellow'
ax_f_c = pyplot.axes([0.10, 0.05, 0.03, 0.65], facecolor=axcolor)
ax_gain = pyplot.axes([0.20, 0.05, 0.03, 0.63], facecolor=axcolor)
ax_type = pyplot.axes([0.05, 0.8, 0.2, 0.15], facecolor=axcolor)

slider_f_c = Slider(ax_f_c, 'Frequency', 100, f_s/2, valinit=f_c, valstep=100, orientation='vertical')
slider_gain = Slider(ax_gain, 'Gain', -12, 12, valinit=gain, valstep=1, orientation='vertical')
type_buttons = RadioButtons(ax_type, ("High-Shelf", "Low-Shelf"))#, orientation='horizontal')

b, a = getShelvingEQ(f_c, gain, shelf_type, f_s) # get filter coefficients
w, h = signal.freqz(b, a, fs=f_s) # calculate impulse response
h_db = 20*numpy.log10(numpy.abs(h)) # dB
ax_EQ.plot(w, h_db)
ax_EQ.set(ylim=[-13, 13], xlabel='Frequenz in Hz', ylabel='Verstärkung in dB', title=f'Shelf-EQ mit Gain = {gain} dB mit Grenzfrequenz f = {f_c} Hz')


# updates the graph once a value has been changed
def update(val):
    '''
    Updates Graph when the parameters are changed through the sliders
    slider values are read in the function not through the input parameter,
    to since it is not known which slider the input parameter belongs to
    
    Parameters:
    -----------
    val : float
        updated slider value (unused)
    '''
    global gain, f_c
    # read silder values and save them globally
    gain = slider_gain.val
    f_c = slider_f_c.val
    b, a = getShelvingEQ(f_c, gain, shelf_type, f_s) # get filter coefficients
    w, h = signal.freqz(b, a, fs=f_s) # calculate impulse response
    h_db = 20*numpy.log10(numpy.abs(h)) # dB    
    ax_EQ.lines[0].remove()
    ax_EQ.plot(w, h_db)
    ax_EQ.set(ylim=[-13, 13], xlabel='Frequenz in Hz', ylabel='Verstärkung in dB', title=f'Shelf-EQ mit Gain = {gain} dB mit Grenzfrequenz f = {f_c} Hz')
    fig.canvas.draw_idle()

slider_f_c.on_changed(update)
slider_gain.on_changed(update)

def change_type(label):
    global shelf_type
    if (label=="Low-Shelf"):
        shelf_type = 0
    else:
        shelf_type = 1
    b, a = getShelvingEQ(f_c, gain, shelf_type, f_s) # get filter coefficients
    w, h = signal.freqz(b, a, fs=f_s) # calculate impulse response
    h_db = 20*numpy.log10(numpy.abs(h)) # dB    
    ax_EQ.lines[0].remove() # deletes the curve
    ax_EQ.plot(w, h_db) # and plots an updated one
    fig.canvas.draw_idle() # call to update the figure

type_buttons.on_clicked(change_type)

pyplot.show()


"""
gain = numpy.linspace(-12, 12, 9)

for idx in range(len(gain)):
    # Low-Shelf
    b, a = getShelvingEQ(f_c_low, gain[idx], 0, f_s)
    w, H = signal.freqz(b, a, worN=128, fs=f_s)
    H_dB = 20*numpy.log10(numpy.abs(H))
    ax_gain.semilogx(w, H_dB)
    
    # High-Shelf
    b, a = getShelvingEQ(f_c_high, gain[idx], 1, f_s)
    w, H = signal.freqz(b, a, worN=128, fs=f_s)
    H_dB = 20*numpy.log10(numpy.abs(H))
    ax_gain.semilogx(w, H_dB)


ax_gain.set(xlabel='Frequenz in Hz', ylabel='20 log_{10} |H(e^{j\Omega})|', title='a) Peak EQ, Parameter ist V_0, f_s = 48kHz')

Freq_low = numpy.linspace(50,4000,6)
Freq_high = numpy.linspace(8000,15000,6)

Gain = 12
for idx in range(len(Freq_low)):
    # Low-Shelf
    b, a = getShelvingEQ(Freq_low[idx], Gain, 0, f_s)
    w, H = signal.freqz(b, a, worN=128, fs=f_s)
    H_dB = 20*numpy.log10(numpy.abs(H))
    ax_f_c.semilogx(w, H_dB)
    
    # High-Shelf
    b, a = getShelvingEQ(Freq_high[idx], Gain, 1, f_s)
    w, H = signal.freqz(b, a, worN=128, fs=f_s)
    H_dB = 20*numpy.log10(numpy.abs(H))
    ax_f_c.semilogx(w, H_dB)

ax_f_c.set(xlabel='Frequenz in Hz', ylabel='20 log_{10} |H(e^{j\Omega})|', title='b) Peak EQ, Parameter ist f_0, f_s = 48kHz')
"""
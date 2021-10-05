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
f_c = 8000
shelf_type = 0

fig, ax_EQ = pyplot.subplots()

b, a = getShelvingEQ(f_c, gain, shelf_type, f_s) # get filter coefficients
w, h = signal.freqz(b, a, fs=f_s) # calculate impulse response
h_db = 20*numpy.log10(numpy.abs(h)) # dB
ax_EQ.plot(w, h_db)
ax_EQ.set(ylim=[-13, 13], xlabel='Frequenz in Hz', ylabel='Verstärkung in dB', title=f'Shelf-EQ mit Gain = {gain} dB mit Grenzfrequenz f = {f_c} Hz')

pyplot.show()

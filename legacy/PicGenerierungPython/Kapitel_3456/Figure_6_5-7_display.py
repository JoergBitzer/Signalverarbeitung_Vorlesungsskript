import matplotlib
import numpy
from scipy import signal
from matplotlib import pyplot
from matplotlib.widgets import Slider

matplotlib.style.use('sv1_style.mplstyle')

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
    
f_s = 48000
freq = 8000
gain = 12
Q = 3

fig, ax_EQ = pyplot.subplots()

b, a = get_peak_EQ(freq, gain, Q, f_s) # get filter coeefficients
w, h = signal.freqz(b, a, fs=f_s) # and calculate transfer function h from it
h_db = 20*numpy.log10(numpy.abs(h)) # dB
ax_EQ.plot(w, h_db)
ax_EQ.set(ylim=[-13, 13], xlabel='Frequenz in Hz', ylabel='Verstärkung in dB', title=f'Peak-EQ mit Gain = {gain} dB bei Frequenz f = {freq} Hz mit Güte Q = {Q:.1f}')

pyplot.show()
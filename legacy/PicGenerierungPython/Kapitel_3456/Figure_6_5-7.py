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
freq = 2000
gain = 5
Q = 1


fig, ax_EQ = pyplot.subplots()
fig.subplots_adjust(left=0.35)

# adds a slider for frequency, gain and Quality Q of the EQ
axcolor = 'lightgoldenrodyellow'
ax_freq = pyplot.axes([0.05, 0.15, 0.03, 0.65], facecolor=axcolor)
ax_gain = pyplot.axes([0.15, 0.15, 0.03, 0.63], facecolor=axcolor)
ax_Q = pyplot.axes([0.25, 0.15, 0.03, 0.65], facecolor=axcolor)

slider_freq = Slider(ax_freq, 'Frequency', 0, f_s/2, valinit=freq, valstep=100, orientation='vertical')
slider_gain = Slider(ax_gain, 'Gain', -12, 12, valinit=gain, valstep=1, orientation='vertical')
slider_Q = Slider(ax_Q, 'Q', 0, 8, valinit=Q, valstep=0.1, orientation='vertical')


b, a = get_peak_EQ(freq, gain, Q, f_s) # get filter coeefficients
w, h = signal.freqz(b, a, fs=f_s) # and calculate transfer function h from it
h_db = 20*numpy.log10(numpy.abs(h)) # dB
ax_EQ.plot(w, h_db)
ax_EQ.set(ylim=[-13, 13], xlabel='Frequenz in Hz', ylabel='Verstärkung in dB', title=f'Peak-EQ mit Gain = {gain} dB bei Frequenz f = {freq} Hz mit Güte Q = {Q:.1f}')

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
    global gain, freq, Q
    # read slider values and sanve them globally
    gain = slider_gain.val
    freq = slider_freq.val
    Q = slider_Q.val
    b, a = get_peak_EQ(freq, gain, Q, f_s) # get filter coefficients 
    w, h = signal.freqz(b, a, fs=f_s) # calculate impulse response
    h_db = 20*numpy.log10(numpy.abs(h)) # dB
    ax_EQ.lines[0].remove() # delete old curve
    ax_EQ.plot(w, h_db) # plot new curve
    ax_EQ.set(ylim=[-13, 13], title=f'Peak-EQ mit Gain = {gain} dB bei Frequenz f = {freq} Hz mit Güte Q = {Q:.1f}')
    fig.canvas.draw_idle() # call to update the figure

# calls "update" when either slider is changed
slider_freq.on_changed(update)
slider_gain.on_changed(update)
slider_Q.on_changed(update)

pyplot.show()

"""
gain = numpy.linspace(-12, 12, 9)

for idx in range(len(gain)):
    b, a = get_peak_EQ(freq, gain[idx], Q, f_s) 
    w, h = signal.freqz(b, a, fs=f_s)
    h_db = 20*numpy.log10(numpy.abs(h))
    ax_gain.semilogx(w, h_db)

ax_gain.set(xlabel='Frequenz in Hz', ylabel='20 log_{10} |H(e^{j\Omega})|', title='Peak EQ, Parameter ist V_0, f_s = 48kHz')

gain = 12
freq = numpy.logspace(2, 4, 8)

for idx in range(len(freq)):
    b, a = get_peak_EQ(freq[idx], gain, Q, f_s)
    w, h = signal.freqz(b, a, fs=f_s)
    h_db = 20*numpy.log10(numpy.abs(h))
    ax_fm.semilogx(w, h_db)

ax_fm.set(xlabel='Frequenz in Hz', ylabel='20 log_{10} |H(e^{j\Omega})|', title='Peak EQ, Parameter ist f_0, f_s = 48kHz')

freq = 2000
Q = numpy.linspace(0.1, 5, 8)

for idx in range(len(Q)):
    b, a = get_peak_EQ(freq, gain, Q[idx], f_s)
    w, h = signal.freqz(b, a, fs=f_s)
    h_db = 20*numpy.log10(numpy.abs(h))
    ax_q.semilogx(w, h_db)

ax_q.set(xlabel='Frequenz in Hz', ylabel='20 log_{10} |H(e^{j\Omega})|', title='Peak EQ, Parameter ist Q, f_s = 48kHz')

Q = 1
"""


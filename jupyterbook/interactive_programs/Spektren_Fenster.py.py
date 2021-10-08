import matplotlib
import numpy
from scipy import signal
from matplotlib import pyplot
from matplotlib.widgets import RadioButtons
from matplotlib.widgets import Slider

matplotlib.style.use('../sv.mplstyle')

N = 32 # window lengths
N_zp = 2048 # length of zero padded window


window = numpy.array([1.0]*N)
window_zp = numpy.concatenate((window, numpy.zeros((N_zp-N))))

# adaptable factors
kaiser_fac = 2
alpha = 0.0
beta = 0.0
gamma = 0.0

spectrum = numpy.fft.fft(window_zp)

mid = numpy.floor(len(spectrum)/2)
# shift area from pi -> 2pi to -pi -> 0
spectrum = numpy.concatenate([spectrum[int(mid):], spectrum[:int(mid)]]) 
# dB maximum = 0dB
spectrum_abs = 20*numpy.log10(numpy.abs(spectrum)/numpy.abs(spectrum).max()) 
freqs_fft = numpy.linspace(-1, 1, len(spectrum_abs)) # freq bins, for plotting

fig, (ax_sample, ax_spectrum) = pyplot.subplots(1, 2)
fig.subplots_adjust(left=0.45)
rax = pyplot.axes([0.05, 0.15, 0.15, 0.75], facecolor='lightgoldenrodyellow')
radio = RadioButtons(rax, ('Rechteck', 'von-Hann', 'Hamming', 
        'Blackman', 'Flat-Top', 'Kaiser', 'Custom'))

fig.subplots_adjust(bottom=0.25)
ax_kaiser = pyplot.axes(
        [0.25, 0.05, 0.65, 0.03], facecolor='lightgoldenrodyellow')
slider_kaiser = Slider(ax_kaiser, 'Kaiser Faktor', 0, 20, 
        valinit=2, valstep=0.1)    

ax_alpha = pyplot.axes(
        [0.25, 0.15, 0.03, 0.75], facecolor='lightgoldenrodyellow')
ax_beta  = pyplot.axes(
        [0.30, 0.15, 0.03, 0.75], facecolor='lightgoldenrodyellow')
ax_gamma = pyplot.axes(
        [0.35, 0.15, 0.03, 0.75], facecolor='lightgoldenrodyellow')

slider_alpha = Slider(ax_alpha, 'alpha', -1, 2, valinit=alpha, 
        valstep=0.01, orientation="vertical")    
slider_beta  = Slider(ax_beta, 'beta', -1, 1, valinit=beta, 
        valstep=0.01, orientation="vertical")    
slider_gamma = Slider(ax_gamma, 'gamma', -1, 1, valinit=gamma, 
        valstep=0.01, orientation="vertical")    

def custom_window_changed(val):
    '''
    updates factors for the custom window calculation 
    and automatically changes display to the custom window
    '''
    global alpha, beta, gamma
    alpha = slider_alpha.val
    beta = slider_beta.val
    gamma = slider_gamma.val
    type_change('Custom')
    
slider_alpha.on_changed(custom_window_changed)
slider_beta.on_changed(custom_window_changed)
slider_gamma.on_changed(custom_window_changed)

def kaiser_factor(val):
    '''
    updates kaiser factor and automatically changes display to kaiser window
    '''
    global kaiser_fac
    kaiser_fac = slider_kaiser.val
    type_change('Kaiser') # change display
    
slider_kaiser.on_changed(kaiser_factor)

def type_change(label):
    '''
    creates certain windows, as can be seen on the button labels
    
    Parameters:
    -----------
    label : str
        button text, indicating the window type to be displayed
    '''
    global window, window_zp, alpha, beta, gamma
    if (label=='Rechteck' or label=='von-Hann' or label=='Hamming' 
            or label=='Blackman' or label=='Custom'):
        if (label=='Rechteck'):
            window = [1.0]*N
        elif(label=='von-Hann'):
            alpha = 0.5
            beta = 0.5
            gamma = 0
            for idx in range(N):
                window[idx] = 0.5 - 0.5*numpy.cos(2*numpy.pi*idx/N)
        elif(label=='Hamming'):
            alpha = 0.54
            beta = 0.46
            gamma = 0
            for idx in range(N):
                window[idx] = 0.54 - 0.46*numpy.cos(2*numpy.pi*idx/N)
        elif(label=='Blackman'):
            alpha = 0.42
            beta = 0.5
            gamma = 0.08
            for idx in range(N):
                window[idx] = 0.42 - 0.5*numpy.cos(2*numpy.pi*idx/N) + \
                        0.08*numpy.cos(4*numpy.pi*idx/N)
        elif(label=='Custom'):
            for idx in range(N):
                window[idx] = alpha + beta*numpy.cos(2*numpy.pi*idx/N) + \
                        gamma*numpy.cos(4*numpy.pi*idx/N)
        window = numpy.array(window)

    elif(label=='Flat-Top'):
        window = signal.windows.flattop(N)
    elif(label=='Kaiser'):
        window = numpy.array(numpy.kaiser(N, kaiser_fac))
  
    # update time domain graph
    graph_sample.set_ydata(window)

    window_zp[:N] = window
    spectrum = numpy.fft.fft(window_zp)
    # shift area from pi -> 2pi to -pi -> 0
    spectrum = numpy.concatenate([spectrum[int(mid):], spectrum[:int(mid)]]) 
    # dB maximum = 0dB
    spectrum_abs = 20*numpy.log10(numpy.abs(spectrum)/numpy.abs(spectrum).max()) 
    # update frequency domain graph
    graph_spectrum.set_ydata(spectrum_abs)
    fig.canvas.draw_idle() # call updates figure
    
radio.on_clicked(type_change)

graph_sample, = ax_sample.plot(window) # saves graph to change it later
ax_sample.set(xlabel='Folgenndex k ->', ylabel='Amplitude x[k]', 
        xlim=[0, 31], ylim=[-0.2, 1.2], title='Zeitbereich')

graph_spectrum, = ax_spectrum.plot(freqs_fft, spectrum_abs)
ax_spectrum.set(xlabel='Frequenz rad/pi ', ylabel='Dämpfung in dB', 
        ylim=[-105, 5], title='Frequenzbereich')

pyplot.show()


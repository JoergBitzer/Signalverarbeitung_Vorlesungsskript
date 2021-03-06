import matplotlib
import numpy
from matplotlib import pyplot
from matplotlib.widgets import RadioButtons

matplotlib.style.use('sv1_style.mplstyle')

# signal that the symmetry is performed on, 
# FEEL FREE TO TRY STUFF OUT HERE!
sig = numpy.array([1, -1])
max_sig = numpy.abs(sig).max()

fig, (ax_sig, ax_spec) = pyplot.subplots(2, 1)
fig.subplots_adjust(left=0.35)
rax = pyplot.axes([0.05, 0.15, 0.20, 0.75], facecolor='lightgoldenrodyellow')
radio = RadioButtons(rax, ('Typ I', 'Typ II', 'Typ III', 'Typ IV'))

ax_sig.stem(sig, use_line_collection=True)
ax_sig.set(xlabel='Folgenkindex k ->', ylabel='Amplitude x(k)', title='Linearphaseige Typen', xlim=([-0.5, len(sig)*2+0.5]))


# zero padding to improve spectral resolution
sig_zp = numpy.append(sig, numpy.zeros((1024, 1)))
spectrum = numpy.fft.fft(sig_zp)

# freqency bin vector, for plotting
w = numpy.linspace(0, 2, len(sig_zp)) 

ax_spec.plot(w, 20 * numpy.log10(abs(spectrum)))
ax_spec.set(xlabel='Frequenz normalisiert mit w/pi', ylabel='Amplitude in dB', title='Spektrum', xlim=([0, 1]), ylim=([-50, 20]))

def type_change(label):
    '''
    Updates the plot according to the chosen symmetry type 
    
    Parameters:
    -----------
    label : str
        button label, indicating the type of symmetry
    '''
    ax_sig.cla()
    sig_reversed = numpy.flip(sig)
    
    if(label=='Typ I'):
        new_sig = numpy.concatenate((sig, sig_reversed[1:]))
    elif(label=='Typ II'):
        new_sig = numpy.concatenate((sig, [0],  -1*sig_reversed))
    elif(label=='Typ III'):
        new_sig = numpy.concatenate((sig, sig_reversed))
    elif(label=='Typ IV'):
        new_sig = numpy.concatenate((sig, -1*sig_reversed))
    ax_sig.stem(new_sig, use_line_collection=True)
    sym_axis = (len(new_sig)-1)/2
    ax_sig.plot((sym_axis, sym_axis), (-max_sig, max_sig), color='r', linestyle='--')
    ax_sig.set(xlabel='Folgenkindex k ->', ylabel='Amplitude x(k)', title='Linearphasige Typen', xlim=([-0.5, len(sig)*2+0.5]))
    
    ax_spec.cla()
    # zero padded foro resolution
    new_sig_zp = numpy.append(new_sig, zero_pad)
    spectrum = numpy.fft.fft(new_sig_zp)
    w = numpy.linspace(0, 2, len(new_sig_zp)) # frequency bins for plotting
    ax_spec.plot(w, 20 * numpy.log10(abs(spectrum)))
    ax_spec.set(xlabel='Frequenz normalisiert mit w/pi', ylabel='Amplitude in dB', title='Spektrum', xlim=([0, 1]), ylim=([-50, 20]))
    
    fig.canvas.draw_idle() # calling this updates the figure

# calls function "lights_change" when button is clicked
radio.on_clicked(type_change)


pyplot.show()

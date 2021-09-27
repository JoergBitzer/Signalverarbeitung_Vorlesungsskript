import matplotlib
import numpy
from matplotlib import pyplot
from matplotlib.widgets import RadioButtons

matplotlib.style.use('sv1_style.mplstyle')

#Hier sieht das Ergebnis grundsätzlich gut aus ist aber noch nicht hoch genug aufgelöst. Ich hätte jetzt einfach Nullen davor und dahinter gepackt, was aber , ist das sinnvoll?

sig = numpy.array([1, -1])
max_sig = numpy.abs(sig).max()

fig, (ax_sig, ax_spec) = pyplot.subplots(2, 1)
fig.subplots_adjust(left=0.35)
rax = pyplot.axes([0.05, 0.15, 0.20, 0.75], facecolor='lightgoldenrodyellow')
radio = RadioButtons(rax, ('Typ I', 'Typ II', 'Typ III', 'Typ IV'))

ax_sig.stem(sig, use_line_collection=True)
ax_sig.set(xlabel='Folgenkindex k ->', ylabel='Amplitude x(k)', title='Linearphaseige Typen', xlim=([-0.5, len(sig)*2+0.5]))




#Nullen dazu um Auflösung zu erhöhen
zero_pad = numpy.zeros((1024, 1))
sig_zp = numpy.append(sig, zero_pad)
spectrum = numpy.fft.fft(sig_zp)

w = numpy.linspace(0, 2, len(sig_zp))

ax_spec.plot(w, 20 * numpy.log10(abs(spectrum)))
ax_spec.set(xlabel='Frequenz normalisiert mit w/pi', ylabel='Amplitude in dB', title='Spektrum', xlim=([0, 1]), ylim=([-50, 20]))

def type_change(label):
    '''
    Wählt richtige Ampelfarbe aus
    '''
    ax_sig.cla()
    sig_rev = numpy.flip(sig)
#    sig_rev_inv = [i * -1 for i in sig_rev]
    print(sig_rev)
    if(label=='Typ I'):
        new_sig = numpy.concatenate((sig, sig_rev[1:]))
    elif(label=='Typ II'):
        new_sig = numpy.concatenate((sig, [0],  -1*sig_rev))
    elif(label=='Typ III'):
        new_sig = numpy.concatenate((sig, sig_rev))
    elif(label=='Typ IV'):
        new_sig = numpy.concatenate((sig, -1*sig_rev))
    ax_sig.stem(new_sig, use_line_collection=True)
    sym_axis = (len(new_sig)-1)/2
    ax_sig.plot((sym_axis, sym_axis), (-max_sig, max_sig), color='r', linestyle='--')
    ax_sig.set(xlabel='Folgenkindex k ->', ylabel='Amplitude x(k)', title='Linearphasige Typen', xlim=([-0.5, len(sig)*2+0.5]))
    
    ax_spec.cla()
    new_sig_zp = numpy.append(new_sig, zero_pad)
    spectrum = numpy.fft.fft(new_sig_zp)
    w = numpy.linspace(0, 2, len(new_sig_zp))
    ax_spec.plot(w, 20 * numpy.log10(abs(spectrum)))
    ax_spec.set(xlabel='Frequenz normalisiert mit w/pi', ylabel='Amplitude in dB', title='Spektrum', xlim=([0, 1]), ylim=([-50, 20]))
    
    fig.canvas.draw_idle()
# ruft "lights_change" auf wenn button gedrückt wurde
radio.on_clicked(type_change)


pyplot.show()

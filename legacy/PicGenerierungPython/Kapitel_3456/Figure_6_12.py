import matplotlib
import numpy
from matplotlib import pyplot

matplotlib.style.use('sv1_style.mplstyle')

samples = numpy.linspace(-100, 100, 201)
si = [0]*len(samples)
mid = int(numpy.floor(len(samples)/2))

fs = 1000
f0 = 100

for idx in range(len(samples)):
    if (samples[idx]!=0):
        si[idx] = numpy.sin(2*numpy.pi * f0 * samples[idx]/fs)/(2*numpy.pi*samples[idx]*f0/fs)
    else:
        # si(0) = 1 to avoid division by zero
        si[idx] = 1

# cut si-function
si_short = si[(mid-25):(mid+25)]
samples_short = samples[(mid-25):(mid+25)]

ax_si = pyplot.subplot(1, 2, 1)
ax_si.plot(samples, si, linestyle='dotted')#,  use_line_collection=True)
ax_si.plot(samples_short, si_short)
ax_si.set(xlabel='Folgenkindex k ->', ylabel='Amplitude x(k)', 
        title='SI-Funktion')
ax_si.set_xlim([-100, 100])

# zero padding, for display resolution
si_short = [0]*100 + si_short + [0]*100
si = [0]*100 + si + [0]*100

spectrum_short = numpy.fft.fft(si_short)
spectrum = numpy.fft.fft(si)

w = numpy.linspace(0, 2, len(si))
w_short = numpy.linspace(0, 2, len(si_short))

ax_spec = pyplot.subplot(1, 2, 2)
ax_spec.plot(w_short, 20 * numpy.log10(abs(spectrum_short)), 
        linestyle='dotted')
ax_spec.plot(w, 20 * numpy.log10(abs(spectrum))) # dB spectrum
ax_spec.set(xlabel='Frequenz normalisiert mit w/pi', ylabel='Amplitude in dB', 
        title='Spektrum', xlim=([0, 0.4]))

pyplot.show()
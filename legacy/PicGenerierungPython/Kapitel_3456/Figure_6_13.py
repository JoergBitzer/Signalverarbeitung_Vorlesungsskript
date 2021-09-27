import matplotlib
import numpy
from scipy import signal
from matplotlib import pyplot


fig, (ax_51, ax_201) = pyplot.subplots(1, 2)
eps = 0.00000000001
f_s = 48000 
f_g = 4800 # 0.2*pi


trans_width = 1200  # Width of transition from pass band to stop band, Hz

# Filterlänge 51
N = 51
idxs = numpy.linspace(numpy.ceil(-N/2), numpy.floor(N/2), N)      # Size of the FIR filter.

# Remez

taps = signal.remez(N, [0, f_g, f_g + trans_width, 0.5*f_s], [1, 0], Hz=f_s)
w, h = signal.freqz(taps, [1], worN=2000)
w = w/numpy.pi

# Rechteck
w_rad = 2*numpy.pi*f_g/f_s
rect_window_51 = w_rad/numpy.pi * numpy.sin(w_rad*idxs+eps)/(w_rad*idxs+eps)
spectrum = numpy.fft.fft(rect_window_51, n=2000)
mid = numpy.floor(len(spectrum)/2)
spectrum = numpy.concatenate([spectrum[int(mid):], spectrum[:int(mid)]])
spectrum_abs = 20*numpy.log10(numpy.abs(spectrum)/numpy.abs(spectrum).max())
freqs_fft = numpy.linspace(-1, 1, len(spectrum_abs))


ax_51.plot(w, 20*numpy.log10(numpy.abs(h)))
#ax_51.plot(w1, 20*numpy.log10(numpy.abs(h1)))
ax_51.plot(freqs_fft, spectrum_abs, linestyle='--')

ax_51.set(xlabel='Frequenz in rad/s', ylabel='Pegel in dB', xlim=[0, 0.4], ylim=[-100, 5], title='Filterlänge 51')

# Filterlänge 201

# Remez
# Filterlänge 51
N = 201
idxs = numpy.linspace(numpy.ceil(-N/2), numpy.floor(N/2), N)      # Size of the FIR filter.

# Remez

taps = signal.remez(N, [0, f_g, f_g + trans_width, 0.5*f_s], [1, 0], Hz=f_s)
w, h = signal.freqz(taps, [1], worN=2000)
w = w/numpy.pi

# Rechteck
w_rad = 2*numpy.pi*f_g/f_s
rect_window_201 = w_rad/numpy.pi * numpy.sin(w_rad*idxs+eps)/(w_rad*idxs+eps)
spectrum = numpy.fft.fft(numpy.concatenate((rect_window_201, [0]*1000)))
mid = numpy.floor(len(spectrum)/2)
spectrum = numpy.concatenate([spectrum[int(mid):], spectrum[:int(mid)]])
spectrum_abs = 20*numpy.log10(numpy.abs(spectrum)/numpy.abs(spectrum).max())
freqs_fft = numpy.linspace(-1, 1, len(spectrum_abs))


ax_201.plot(w, 20*numpy.log10(numpy.abs(h)))
ax_201.plot(freqs_fft, spectrum_abs, linestyle='--')
ax_201.set(xlabel='Frequenz in rad/s', ylabel='Pegel in dB', xlim=[0, 0.4], ylim=[-100, 5], title='Filterlänge 201')

pyplot.show()
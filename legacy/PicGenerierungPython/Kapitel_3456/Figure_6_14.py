import matplotlib
import numpy
from scipy import signal
from matplotlib import pyplot

#matplotlib.style.use('sv1_style.mplstyle')


fig, (ax_51, ax_201) = pyplot.subplots(1, 2)

eps = numpy.finfo(float).eps # for slight offset to avoid division by 0
f_s = 48000 
f_g = 4800 # Hz, cuttoff frequency

trans_width = 1200  # Hz, Width of transition from pass band to stop band

# filter length 51
N = 51      # Size of the FIR filter.
idxs = numpy.linspace(numpy.ceil(-N/2), numpy.floor(N/2), N)

# Remez filter design
taps = signal.remez(N, [0, f_g, f_g + trans_width, 0.5*f_s], [1, 0], Hz=f_s)
w, h = signal.freqz(taps, [1], worN=2000)
w = w/numpy.pi

# Von Hann filter design
w_rad = 2*numpy.pi*f_g/f_s # cutoff freq in rang od 0 -> 2*pi
# designing the filter
rect_window_51 = w_rad/numpy.pi * numpy.sin(w_rad*idxs+eps)/(w_rad*idxs+eps)
von_hann_window = [0]*N
for idx in range(N):
    von_hann_window[idx] = 0.5 - 0.5*numpy.cos(2*numpy.pi*idx/N)
window_51 = numpy.array(rect_window_51) * numpy.array(von_hann_window)
spectrum = numpy.fft.fft(numpy.concatenate((window_51, [0]*1000)))
mid = numpy.floor(len(spectrum)/2)
# shift area from pi -> 2pi to -pi -> 0
spectrum = numpy.concatenate([spectrum[int(mid):], spectrum[:int(mid)]]) 
# dB maximum = 0dB
spectrum_abs = 20*numpy.log10(numpy.abs(spectrum)/numpy.abs(spectrum).max()) 
freqs_fft = numpy.linspace(-1, 1, len(spectrum_abs)) # freq bins, for plotting

ax_51.plot(w, 20*numpy.log10(numpy.abs(h)))
ax_51.plot(freqs_fft, spectrum_abs, linestyle='--')
ax_51.set(xlabel='Frequenz in rad/s', ylabel='Pegel in dB', xlim=[0, 0.4], 
        ylim=[-100, 5], title='Filterlänge 51')

# filter length 201
# -----------------
N = 201     # Size of the FIR filter.
idxs = numpy.linspace(numpy.ceil(-N/2), numpy.floor(N/2), N)

taps = signal.remez(N, [0, f_g, f_g + trans_width, 0.5*f_s], [1, 0], Hz=f_s)
w, h = signal.freqz(taps, [1], worN=2000)
w = w/numpy.pi
# Von Hann
w_rad = 2*numpy.pi*f_g/f_s # cutoff freq in rang od 0 -> 2*p
# designing the filter
rect_window_51 = w_rad/numpy.pi * numpy.sin(w_rad*idxs+eps)/(w_rad*idxs+eps)
von_hann_window = [0]*N
for idx in range(N):
    von_hann_window[idx] = 0.5 - 0.5*numpy.cos(2*numpy.pi*idx/N)
window_201 = numpy.array(rect_window_51) * numpy.array(von_hann_window)
spectrum = numpy.fft.fft(numpy.concatenate((window_201, [0]*1000)))
mid = numpy.floor(len(spectrum)/2)
# shift area from pi -> 2pi to -pi -> 0
spectrum = numpy.concatenate([spectrum[int(mid):], spectrum[:int(mid)]]) 
# dB maximum = 0dB
spectrum_abs = 20*numpy.log10(numpy.abs(spectrum)/numpy.abs(spectrum).max()) 
freqs_fft = numpy.linspace(-1, 1, len(spectrum_abs)) # freq bins, for plotting


ax_201.plot(w, 20*numpy.log10(numpy.abs(h)))
ax_201.plot(freqs_fft, spectrum_abs, linestyle='--')
ax_201.set(xlabel='Frequenz in rad/s', ylabel='Pegel in dB', xlim=[0, 0.4], 
        ylim=[-100, 5], title='Filterlänge 201')

pyplot.show()
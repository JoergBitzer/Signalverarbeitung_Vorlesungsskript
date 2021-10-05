import matplotlib
import numpy
from matplotlib import pyplot

matplotlib.style.use('sv1_style.mplstyle')


N = 32 # window length

# calculate window samples by sample
hamming_window = [0]*N 
for idx in range(N):
    hamming_window[idx] = 0.54 - 0.46*numpy.cos(2*numpy.pi*idx/N)

hamming_window = numpy.concatenate([hamming_window, [0]*100000]) # zero padding

spectrum = numpy.fft.fft(hamming_window)
mid = numpy.floor(len(spectrum)/2)
# shift area from pi -> 2pi to -pi -> 0
spectrum = numpy.concatenate([spectrum[int(mid):], spectrum[:int(mid)]]) 
# dB maximum = 0dB
spectrum_abs = 20*numpy.log10(numpy.abs(spectrum)/numpy.abs(spectrum).max()) 
freqs_fft = numpy.linspace(-1, 1, len(spectrum_abs)) # freq bins, for plotting

# time plot
fig, (ax_sample, ax_spectrum) = pyplot.subplots(1, 2)
ax_sample.plot(hamming_window)
ax_sample.set(xlabel='Folgenndex k ->', ylabel='Amplitude x[k]', xlim=[0, N-1],
        title='Hamming-Fenster im Zeitbereich')

# spectral plot
ax_spectrum.plot(freqs_fft, spectrum_abs)
ax_spectrum.set(xlabel='Frequenz rad/pi ', ylabel='Dämpfung in dB', 
        title='Hamming-Fenster im Frequenzbereich')

pyplot.show()


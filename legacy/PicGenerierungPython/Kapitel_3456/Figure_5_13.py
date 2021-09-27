import matplotlib
import numpy
from matplotlib import pyplot

matplotlib.style.use('sv1_style.mplstyle')


N = 32 # Fensterlänge
hamming_window = [0]*N # Fenstervektor
# berechnet Fenster
for idx in range(N):
    hamming_window[idx] = 0.54 - 0.46*numpy.cos(2*numpy.pi*idx/N)

hamming_window = numpy.concatenate([hamming_window, [0]*100000]) # nullen hinzufügen

spectrum = numpy.fft.fft(hamming_window)
mid = numpy.floor(len(spectrum)/2)
spectrum = numpy.concatenate([spectrum[int(mid):], spectrum[:int(mid)]]) # spektrum von pi bis 2*pi wird in den negativen Bereich verschoben
spectrum_abs = 20*numpy.log10(numpy.abs(spectrum)/numpy.abs(spectrum).max()) # dB von Spektrum
freqs_fft = numpy.linspace(-1, 1, len(spectrum_abs)) # Frequenz von -1 bis 1 in rad/pi

# Fensterplot
fig, (ax_sample, ax_spectrum) = pyplot.subplots(1, 2)
ax_sample.plot(hamming_window)
ax_sample.set(xlabel='Folgenndex k ->', ylabel='Amplitude x[k]', xlim=[0, N-1], title='Hamming-Fenster im Zeitbereich')

# Spektraler Plot
ax_spectrum.plot(freqs_fft, spectrum_abs)
ax_spectrum.set(xlabel='Frequenz rad/pi ', ylabel='Dämpfung in dB', title='Hamming-Fenster im Frequenzbereich')

pyplot.show()


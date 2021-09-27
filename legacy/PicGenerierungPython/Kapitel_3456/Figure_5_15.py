import matplotlib
import numpy
from scipy import signal
from matplotlib import pyplot

matplotlib.style.use('sv1_style.mplstyle')

N = 32

dolph_cheb_win = signal.windows.chebwin(N, at=40)
dolph_cheb_win = numpy.concatenate([dolph_cheb_win, [0]*1000])


spectrum = numpy.fft.fft(dolph_cheb_win)
mid = numpy.floor(len(spectrum)/2)
spectrum = numpy.concatenate([spectrum[int(mid):], spectrum[:int(mid)]])
spectrum_abs = 20 * numpy.log10(numpy.abs(spectrum)/numpy.abs(spectrum).max())
freqs_fft = numpy.linspace(-1, 1, len(spectrum_abs))

fig, (ax_sample, ax_spectrum) = pyplot.subplots(1, 2)
ax_sample.plot(dolph_cheb_win)
ax_sample.set(xlabel='Folgenndex k ->', ylabel='Amplitude x[k]', xlim=[0, N-1], title='Dolph-Chebbychev-Fenster im Zeitbereich')

ax_spectrum.plot(freqs_fft, spectrum_abs)
ax_spectrum.set(xlabel='Frequenz rad/pi ', ylabel='Dämpfung in dB', title='Dolph-Chebbychev-Fenster im Frequenzbereich')

pyplot.show()


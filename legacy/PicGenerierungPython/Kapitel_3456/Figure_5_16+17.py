import matplotlib
import numpy
from matplotlib import pyplot

matplotlib.style.use('sv1_style.mplstyle')

N = 32

k4_window = numpy.kaiser(N, 4)
k2_window = numpy.kaiser(N, 2)
k4_window = numpy.concatenate([k4_window, [0]*1000])
k2_window = numpy.concatenate([k2_window, [0]*1000])


spectrum_k4 = numpy.fft.fft(k4_window)
spectrum_k2 = numpy.fft.fft(k2_window)

mid = numpy.floor(len(spectrum_k4)/2)

spectrum_k4 = numpy.concatenate([spectrum_k4[int(mid):], spectrum_k4[:int(mid)]])
spectrum_k2 = numpy.concatenate([spectrum_k2[int(mid):], spectrum_k2[:int(mid)]])
spectrum_k4_abs = 20*numpy.log10(numpy.abs(spectrum_k4)/numpy.abs(spectrum_k4).max())
spectrum_k2_abs = 20*numpy.log10(numpy.abs(spectrum_k2)/numpy.abs(spectrum_k2).max())
freqs_fft_k4 = numpy.linspace(-1, 1, len(spectrum_k4_abs))
freqs_fft_k2 = numpy.linspace(-1, 1, len(spectrum_k2_abs))

fig1, (ax_sample_k4, ax_spectrum_k4) = pyplot.subplots(1, 2)
ax_sample_k4.plot(k4_window)
ax_spectrum_k4.plot(freqs_fft_k4, spectrum_k4_abs)
ax_sample_k4.set(xlabel='Folgenndex k ->', ylabel='Amplitude x[k]', xlim=[0, N-1], title='Kaiser-Fenster (beta = 4) im Zeitbereich')
ax_spectrum_k4.set(xlabel='Frequenz rad/pi ', ylabel='Dämpfung in dB', title='Kaiser-Fenster (beta = 4) im Frequenzbereich')


fig2, (ax_sample_k2, ax_spectrum_k2) = pyplot.subplots(1, 2)
ax_sample_k2.plot(k2_window)
ax_spectrum_k2.plot(freqs_fft_k2, spectrum_k2_abs)
ax_sample_k2.set(xlabel='Folgenndex k ->', ylabel='Amplitude x[k]', xlim=[0, N-1], title='Kaiser-Fenster (beta = 2) im Zeitbereich')
ax_spectrum_k2.set(xlabel='Frequenz rad/pi ', ylabel='Dämpfung in dB', title='Kaiser-Fenster (beta = 2) im Frequenzbereich')

pyplot.show()


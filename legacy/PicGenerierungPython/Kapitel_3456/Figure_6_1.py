import matplotlib
import numpy
import scipy
from scipy import signal
from matplotlib import pyplot

matplotlib.style.use('sv1_style.mplstyle')
Fs = 8000
fg = 1000
x = [0.0]*Fs
x[0] = 1.0
b, a = scipy.signal.butter(N=6, Wn=fg, btype='low', output='ba', fs=Fs)
y = scipy.signal.lfilter(b, a, x)
spectrum = numpy.fft.fft(y)
#mid = numpy.floor(len(spectrum)/2)
#spectrum = numpy.concatenate([spectrum[int(mid):], spectrum[:int(mid)]])
spectrum_abs = 20*numpy.log10(numpy.abs(spectrum)/numpy.abs(spectrum).max())
freq_vec = numpy.linspace(0, Fs, len(spectrum_abs))

fig, ax_spectrum = pyplot.subplots()

ax_spectrum.step(y=[0, 0, -100, - 100, 0], x=[0, fg, Fs/2, Fs-fg, Fs], color='b', label="Optimale Entwurfsvorgabe")
ax_spectrum.plot(freq_vec, spectrum_abs, color='r', label="Mögliche Realisierung")

ax_spectrum.set(xlabel='Frequenz in Hz ', ylabel='Dämpfung in dB', xlim=[0, Fs/2], ylim=[-105, 5], title='Tiefpass')
pyplot.legend()


pyplot.show()
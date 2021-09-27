import matplotlib
import numpy
from matplotlib import pyplot

matplotlib.style.use('sv1_style.mplstyle')

num_samples = 16
f0 = 155
fs = 1000

sample = [0]*num_samples

for idx in range(num_samples):
    sample[idx] = numpy.cos(2*numpy.pi*f0*idx/fs)

sample = numpy.concatenate([[0]*4 + sample + [0]*4])
spectrum = numpy.fft.fft(sample)
spectrum_abs = numpy.abs(spectrum)/numpy.abs(spectrum).max()
ifft = numpy.fft.ifft(spectrum)


freqs_fft = numpy.linspace(-1, 1, len(spectrum_abs))

# Bild 5.6
f1, (ax_sample, ax_spectrum) = pyplot.subplots(1, 2)
ax_sample.plot(sample)
ax_sample.set(xlabel='Folgenndex k ->', ylabel='Amplitude x[k]', title='Eingangssignal Sinus')

ax_spectrum.plot(freqs_fft, spectrum_abs)
ax_spectrum.set(xlabel='Frequenz rad/pi ', ylabel='Frequenzanteil normiert auf 1', title='Spektrum eines Rechteckfenster (Dirichlet-Funktion)')

# Bild 5.7
f2, (ax_spec_stem, ax_ifft) = pyplot.subplots(1, 2)
ax_spec_stem.stem(freqs_fft, spectrum_abs, use_line_collection=True)
ax_spec_stem.set(xlabel='Frequenz rad/pi ', ylabel='Frequenzanteil normiert auf 1', title='Spektrum eines Rechteckfenster (Dirichlet-Funktion)')

ax_ifft.plot(ifft)
ax_ifft.set(xlabel='Folgenndex k ->', ylabel='Amplitude x[k]', title='durch inverse FFT rekonstruiertes Signal')

pyplot.show()

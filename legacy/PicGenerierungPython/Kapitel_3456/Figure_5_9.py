import matplotlib
import numpy
from matplotlib import pyplot

matplotlib.style.use('sv1_style.mplstyle')

# input samples
a = [1, 2, 3, 4, 5, 6, 7, 8]
b = [1, 2, 3, 4, -1, -2, -3, -4]

# usual convolution
usual_convolution = numpy.convolve(a, b)

# cyclical convolution, equal to multiplying spectra
dft_spektrum = numpy.fft.fft(a) * numpy.fft.fft(b)
zyklische_faltung = numpy.fft.ifft(dft_spektrum)


fig, ((ax_a, ax_b), (ax_ab, ax_fft)) = pyplot.subplots(2, 2)

ax_a.stem(a, use_line_collection=True)
ax_a.set(xlabel='Folgenndex k ->', ylabel='Amplitude x[k]', title='Signal A')
ax_b.stem(b, use_line_collection=True)
ax_b.set(xlabel='Folgenndex k ->', ylabel='Amplitude x[k]', title='Signal B')
ax_ab.stem(konventionelle_faltung, use_line_collection=True)
ax_ab.set(xlabel='Folgenndex k ->', ylabel='Amplitude', 
        title='Konventionelle Faltung')
ax_fft.stem(zyklische_faltung, use_line_collection=True)
ax_fft.set(xlabel='Folgenndex k ->', ylabel='Amplitude', 
        title='Zyklische Faltung')

pyplot.show()
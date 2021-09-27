import matplotlib
import numpy
from matplotlib import pyplot

matplotlib.style.use('sv1_style.mplstyle')

N = 16
freqs = numpy.linspace(-3, 3, 600)
dirichlet = [0]*len(freqs)
for idx in range(len(freqs)):
    dirichlet[idx] = numpy.sin(N*freqs[idx]*numpy.pi*0.5)/numpy.sin(freqs[idx]*numpy.pi*0.5)

dirichlet_abs = numpy.abs(dirichlet)/numpy.abs(dirichlet).max()

ax_dirichlet = pyplot.subplot()
ax_dirichlet.plot(freqs, dirichlet_abs)
ax_dirichlet.set(xlabel='Frequenz rad/pi ', ylabel='Frequenzanteil normiert auf 1', title='Spektrum eines Rechteckfenster (Dirichlet-Funktion)')

pyplot.show()
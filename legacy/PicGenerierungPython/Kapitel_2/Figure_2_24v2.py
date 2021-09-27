import matplotlib
import numpy
from matplotlib import pyplot

matplotlib.style.use('sv1_style.mplstyle')
N = 20000
stufen = numpy.linspace(-10, 10, 41)

fig, (ax_gleichv, ax_standard_normv, ax_normv) = pyplot.subplots(1, 3, sharey='row')
ax_gleichv.set_xlim([-10, 10])

gleichv = numpy.random.uniform(low=-4, high=4, size=N)
ax_gleichv.hist(gleichv, stufen)
ax_gleichv.set(title='Gleichverteilung von -4 bis 4', ylabel='Anzahl Werte pro Bin')

standard_normv = numpy.random.standard_normal(size=N)
ax_standard_normv.hist(standard_normv, stufen)
ax_standard_normv.set(title='Standardnormalvertelung mu=0 rho^2=1')

normv = numpy.random.normal(loc=1.0, scale=3.0, size=N)
ax_normv.hist(normv, stufen)
ax_normv.set(title='Normalverteilung mu=1 rho^2=3')

pyplot.show()

import matplotlib
import numpy
from matplotlib import pyplot

# determine where we're running from and set paths accordingly
try: 
    if get_ipython().__class__.__name__ == 'ZMQInteractiveShell':
        prefix = ''
except:
    prefix = '../../'

matplotlib.style.use(f'{prefix}sv.mplstyle')

N = 20000 # number of random samples for distribution
bins = numpy.linspace(-10, 10, 41) # 41 equal spaced bins between -10 and 10

N = 20000
stufen = numpy.linspace(-10, 10, 41)

fig, (ax_gleichv, ax_standard_normv, ax_normv) = pyplot.subplots(1, 3)
ax_gleichv.set_xlim([-10, 10])

# generating random data
uniform = numpy.random.uniform(low=-4, high=4, size=N)
# standardized normal mu=0, sigma=1
standard_normal = numpy.random.standard_normal(size=N) 
# normal mu = 1, sigma = 3
normal = numpy.random.normal(loc=1.0, scale=3.0, size=N)
ax_gleichv.hist(uniform, bins)
ax_gleichv.set(xlim=[-10, 10], ylim=[0, 4000], title='Gleichverteilung \n von -4 bis 4', 
        ylabel='Anzahl Werte pro Bin')


standard_normv = numpy.random.standard_normal(size=N)
ax_standard_normv.hist(standard_normv, stufen)
ax_standard_normv.set(title='Standardnormalverteilung \n' +r'$\mu=0$, $\sigma^2=1$', ylim=[0, 4000])

normv = numpy.random.normal(loc=1.0, scale=3.0, size=N)
ax_normv.hist(normv, stufen)
ax_normv.set(title='Normalverteilung \n' + r'$\mu=1$, $\sigma^2=3$', ylim=[0, 4000])
pyplot.tight_layout()

pyplot.show()

# glue this figure to paste it later (no effect outside of MyST NB)
from myst_nb import glue
glue("Verteilungen", fig, display=False)
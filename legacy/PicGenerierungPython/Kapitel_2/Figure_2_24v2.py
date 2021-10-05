import matplotlib
import numpy
from matplotlib import pyplot

matplotlib.style.use('sv1_style.mplstyle')
N = 20000 # number of random samples for distribution
bins = numpy.linspace(-10, 10, 41) # 41 equal spaced bins between -10 and 10

fig, (ax_uniform, ax_standard_normal, ax_normal) = pyplot.subplots(
        1, 3, sharey='row')

# generating random data
uniform = numpy.random.uniform(low=-4, high=4, size=N)
# standardized normal mu=0, sigma=1
standard_normal = numpy.random.standard_normal(size=N) 
# normal mu = 1, sigma = 3
normal = numpy.random.normal(loc=1.0, scale=3.0, size=N)
ax_uniform.hist(uniform, bins)
ax_uniform.set(xlim=[-10, 10], title='Gleichverteilung \n von -4 bis 4', 
        ylabel='Anzahl Werte pro Bin')

ax_standard_normal.hist(standard_normal, bins)
ax_standard_normal.set(title='Standardnormalvertelung \n mu=0 rho^2=1')

ax_normal.hist(normal, bins)
ax_normal.set(title='Normalverteilung \n mu=1 rho^2=3')

pyplot.show()
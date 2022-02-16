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

# defining linear and non linear input vectors and linear output
input_lin = numpy.linspace(-1, 1, 2**4)
input_nlin = input_lin**3
output = numpy.linspace(-1+2**-5, 1-2**-5, 2**4)

#plot linear quantizer
fig, (ax_lin, ax_nlin) = pyplot.subplots(1, 2)
ax_lin.step(input_lin, output, where='mid', linewidth=2) # defines the steps of a step diagram
ax_lin.plot([-2, 2], [-2, 2], 'o--', color='blue', alpha=0.5, linewidth=2)
ax_lin.set(xlabel='input', ylabel='output', title='Linearer Quantisierer', xlim=[-1, 1], ylim=[-1, 1])

#plot non-linear quantizer
ax_nlin.step(input_nlin, output, where='mid', linewidth=2) # defines the steps of a step diagram
ax_nlin.plot([-2, 2], [-2, 2], 'o--', color='blue', alpha=0.5, linewidth=2)
ax_nlin.set(xlabel='input', ylabel='output', title='Nicht-linearer Quantisierer', xlim=[-1, 1], ylim=[-1, 1])

pyplot.show()

# glue this figure to paste it later (no effect outside of MyST NB)
from myst_nb import glue
glue("NonLinearQuant", fig, display=False)
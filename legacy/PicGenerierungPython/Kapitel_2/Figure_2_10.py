import matplotlib
import numpy
from matplotlib import pyplot

matplotlib.style.use('sv1_style.mplstyle')

bits = 2 # number of bits used to quantize, feel free to change this

# calculating the vectors to plot 
input_midrise = numpy.linspace(-1 + (1/2**(bits-1)), 1, 2**bits)
output_midrise = numpy.linspace(-1 + 2**-bits, 1 - (1/2**bits), 2**bits)

input_midtread = numpy.linspace(-1 + (1/2**bits), 1 - (1/2**bits), 2**bits)
output_midtread = numpy.linspace(-1, 1 - (1/2**(bits-1)), 2**bits)

# appending  limiting values to the edges of the vector,
# this is purely for displaying purposes, to avoid a misleading
# end of quantization after the last calculated values
input_midrise = numpy.concatenate([[-2], input_midrise, [2]])
input_midtread = numpy.concatenate([[-2], input_midtread, [2]])
output_midrise = numpy.concatenate(
        [[-1 + 2**-bits], output_midrise, [1 - (1/2**bits)]])
output_midtread = numpy.concatenate(
        [[-1], output_midtread, [1 - (1/2**(bits-1))]])

# plots the quantizer lines as step diagrams
ax_rise = pyplot.subplot(1, 2, 1)
ax_rise.step(input_midrise, output_midrise, where='pre', linewidth=2)
ax_rise.plot([-2, 2], [-2, 2], 'o--', color='blue', alpha=0.5, linewidth=2)
ax_rise.set(xlabel='input', ylabel='output', title='Mid-Rise Quantisierer', 
        xlim=[-2, 2], ylim=[-1, 1])

ax_tread = pyplot.subplot(1, 2, 2)
ax_tread.step(input_midtread, output_midtread, where='pre', linewidth=2)
ax_tread.plot([-2, 2], [-2, 2], 'o--', color='blue', alpha=0.5, linewidth=2)
ax_tread.set(xlabel='input', ylabel='output', title='Mid-Tread Quantisierer', 
        xlim=[-2, 2], ylim=[-1, 1])

pyplot.show()
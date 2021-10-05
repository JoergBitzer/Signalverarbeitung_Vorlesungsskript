import matplotlib
import numpy
from matplotlib import pyplot

# this script only consist of plotting predifinded vectors
# and the convolution of them with the system

matplotlib.style.use('sv1_style.mplstyle')

index = [0, 1, 2, 3, 4, 5, 6]
x = [1, 0.5, 1]
x0 = [1, 0, 0]
x1 = [0, 0.5, 0]
x2 = [0, 0, 1]
system = [0.5, 0.75, 1]

y_x_0 = numpy.convolve(x0, system)
y_x_1 = numpy.convolve(x1, system)
y_x_2 = numpy.convolve(x2, system)
conv_sum = numpy.convolve(x, system)


fig, ((ax_input, ax_system),(ax_x0, ax_yx0),(ax_x1, ax_yx1),(ax_x2, ax_yx2),
        (ax_empty, ax_sum)) = pyplot.subplots(5, 2, sharex='all', sharey='all')


ax_input.stem(x + [0, 0], use_line_collection=True)
ax_input.set(xlabel='Folgenindex k ->', ylabel='Amplitude x[k]', 
        title='Inputsignal', xlim=[-0.5, 6.5], ylim=[0, 2])

ax_system.stem(system + [0, 0], use_line_collection=True)
ax_system.set(xlabel='Folgenindex k ->', ylabel='Amplitude x[k]', 
        title='System', xlim=[-0.5, 6.5], ylim=[0, 2])

ax_x0.stem(x0, use_line_collection=True)
ax_x0.set(xlabel='Folgenindex k ->', ylabel='Amplitude x[k]', 
        title='Input bei x[0]', xlim=[-0.5, 6.5], ylim=[0, 2])

ax_yx0.stem(y_x_0, use_line_collection=True)
ax_yx0.set(xlabel='Folgenindex k ->', ylabel='Amplitude x[k]', 
        title='Systemantwort für x[0]', xlim=[-0.5, 6.5], ylim=[0, 2])


ax_x1.stem(x1, use_line_collection=True)
ax_x1.set(xlabel='Folgenindex k ->', ylabel='Amplitude x[k]', 
        title='Input bei x[1]', xlim=[-0.5, 6.5], ylim=[0, 2])


ax_yx1.stem(y_x_1, use_line_collection=True)
ax_yx1.set(xlabel='Folgenindex k ->', ylabel='Amplitude x[k]', 
        title='Systemantwort für x[1]', xlim=[-0.5, 6.5], ylim=[0, 2])


ax_x2.stem(x2, use_line_collection=True)
ax_x2.set(xlabel='Folgenindex k ->', ylabel='Amplitude x[k]', 
        title='Input bei x[2]', xlim=[-0.5, 6.5], ylim=[-0, 2])

ax_yx2.stem(y_x_2, use_line_collection=True)
ax_yx2.set(xlabel='Folgenindex k ->', ylabel='Amplitude x[k]', 
        title='Systemantwort für x[2]', xlim=[-0.5, 6.5], ylim=[0, 2])

ax_sum.stem(conv_sum, use_line_collection=True)
ax_sum.set(xlabel='Folgenindex k ->', ylabel='Amplitude x[k]', 
        title='Systemantwort für Inputsignal', xlim=[-0.5, 6.5], ylim=[0, 2])

pyplot.show()
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Demoscript for "Signalverarbeitung 1"
#
# Version: 1.0   17.02.2022
# 
# This software is released as public domain under CC0 1.0
# https://creativecommons.org/publicdomain/zero/1.0/
#-------------------------------------------------------------------------------

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

def impulse(num_samples, pole):
    r_pole = (pole.real**2 + pole.imag**2)**0.5 
    phi_pole = numpy.angle(pole) # in rad/s
    A = -1j*(numpy.exp(1j*phi_pole))/(2*numpy.sin(phi_pole))
    r_A = numpy.abs(A)
    phi_A = numpy.angle(A)
    y = numpy.zeros(num_samples)
    for idx in range(num_samples):
        y[idx] = 2 * r_A * r_pole**idx * numpy.cos(phi_pole*idx + phi_A)
    return y

def onclick(event):
    ax_pz.lines[1].remove()
    ax_imp.cla()

    pole = event.xdata + 1j*event.ydata
    y = impulse(50, pole)
    
    ax_pz.plot([pole.real, pole.real], [pole.imag, -pole.imag], marker='X', linestyle='none', color='blue')
    ax_imp.stem(y, use_line_collection=True)
    ax_imp.set(xlabel='Folgenkindex k ->', ylabel='Amplitude', title=f'Impulsantwort des Systems', xlim=[0, num_samples-1], ylim=[-y.max(), y.max()])
    fig.canvas.draw_idle()



theta = numpy.linspace(0, 2*numpy.pi, 100)
circle = numpy.exp(1j*theta)
pole = 0.8560 + 0.2781j

fig, (ax_pz, ax_imp)= pyplot.subplots(1, 2)

# Pole-Zero Plot
ax_pz.axis('equal')
ax_pz.set(xlabel=r'Realteil', ylabel=r'Imaginärteil', title='Pol-Nullstellen-Plan', xlim=[-1.5, 1.5], ylim=[-1.5, 1.5])
ax_pz.plot(circle.real, circle.imag)
ax_pz.plot([pole.real, pole.real], [pole.imag, -pole.imag], marker='X', linestyle='none', color='blue')

num_samples = 50
y = impulse(num_samples, pole)


# Impulse Plot
ax_imp.stem(y, use_line_collection=True)
ax_imp.set(xlabel=r'Folgenkindex $k \rightarrow$ ', ylabel='Amplitude', title='Impulsantwort des Systems', xlim=[0, num_samples-1])

cid = fig.canvas.mpl_connect('button_press_event', onclick)

pyplot.show()

# glue this figure to paste it later (no effect outside of MyST NB)
from myst_nb import glue
glue("BspKonjKomplexPole", fig, display=False)
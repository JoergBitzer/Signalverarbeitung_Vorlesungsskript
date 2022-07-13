# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Demoscript for "Signalverarbeitung 1"
#
# Version: 1.0   17.02.2022
# 
# This software is released as public domain under CC0 1.0
# https://creativecommons.org/publicdomain/zero/1.0/
#-------------------------------------------------------------------------------

# based on https://matplotlib.org/3.1.0/gallery/mplot3d/surface3d_radial.html 

"""
Dem Polnullstellenplan kann per Rechtsklick eine Nullstelle, und per Linksklick eine Pollstelle hinzugefügt werden. Um eine Pol- / Nullstelle zu löschen muss man während man auf sie klickt 'Strg' halten. Es werden automatisch die konjugierten Pol- / Nullstellen hinzugefügt und gelöscht
"""

from mpl_toolkits.mplot3d import Axes3D
import numpy
import matplotlib
from matplotlib import pyplot
from matplotlib import cm

# determine where we're running from and set paths accordingly
try: 
    if get_ipython().__class__.__name__ == 'ZMQInteractiveShell':
        prefix = ''
except:
    prefix = '../../'

matplotlib.style.use(f'{prefix}sv.mplstyle')

def H_from_pole_zero(C):
    zaehler = numpy.ones_like(C)
    nenner = numpy.ones_like(C)

    for idx in range(len(zeros)):
        null = numpy.multiply(C - zeros[idx], C - numpy.conjugate(zeros[idx]))
        zaehler = numpy.multiply(zaehler, null)
        
    for idx in range(len(poles)):
        pole = numpy.multiply(C - poles[idx], C - numpy.conjugate(poles[idx]))
        nenner = numpy.multiply(nenner, pole)

    H = zaehler/(nenner+0.0000001)
    Z = 20*numpy.log10(numpy.abs(H))
    max_val = 60
    Z[Z>max_val]=max_val
    Z[Z<-max_val] = -max_val
    return Z

# Create the mesh in polar coordinates and compute corresponding Z.
theta = numpy.linspace(0, 2*numpy.pi, 100)
circle = numpy.exp(1j*theta)

x = numpy.linspace(-1.5, 1.5, 100)
y = numpy.linspace(-1.5j, 1.5j, 100)

poles = [0.8560 + 0.2781j]
zeros = [-1+0j]
#poles_conj = [0]*2
#zeros_conj = [0]*2
fig = pyplot.figure()
ax_pz = fig.add_subplot(121)

ax_pz.plot(circle.real, circle.imag)
ax_pz.set(xlabel=r'Realteil', ylabel=r'Imaginärteil', 
          title='Pol-Nullstellen-Plan', xlim=[-1.5, 1.5], ylim=[-1.5, 1.5])
ax_pz.axis('equal')

for idx in range(len(poles)):
    ax_pz.plot([poles[idx].real, poles[idx].real], [poles[idx].imag, -poles[idx].imag], marker='X', linestyle='none', color='red')
    ax_pz.plot([zeros[idx].real, zeros[idx].real], [zeros[idx].imag, -zeros[idx].imag], marker='o', linestyle='none', color='blue')

ax_pz.text(-0.95,-0.1,"2", color = 'blue', fontsize = 7)


X, Y = numpy.meshgrid(x, y)
C = X + Y

Z = H_from_pole_zero(C)

Y = Y.imag

ax_3d = fig.add_subplot(122, projection='3d')
ax_3d.plot_surface(X,Y,Z, cmap=cm.coolwarm, alpha=0.8)
X_c = circle.real
Y_c = circle.imag
Z_c = H_from_pole_zero(circle)

ax_3d.plot(X_c, Y_c, Z_c, color='black')

ax_3d.set(xlim=[-1.5, 1.5], ylim=[-1.5, 1.5], zlim=[-60, 60])
ax_3d.set_xlabel('Realteil')
ax_3d.set_ylabel('Imaginärteil')
ax_3d.set_zlabel(r'$H$ in dB')

pyplot.show()

# glue this figure to paste it later (no effect outside of MyST NB)
from myst_nb import glue
glue("PolNullstellenplan", fig, display=False)
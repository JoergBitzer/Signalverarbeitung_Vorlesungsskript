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

def quantize_midtread (x, bits):
    scale_factor = 2**(bits-1)
    out = x*scale_factor
    out = numpy.floor(out + 0.5)
    out = out/scale_factor
    index = out > 1. - 1./(2**(bits-1))
    out[index] = 1. - 1./(2**(bits-1))
    return out 
    

bits = 8
fs_cont = 100000
fs = 2000
f0 = 100
steps = int(fs_cont/fs)
T = 0.02
t = numpy.linspace(0, T, round(T*fs_cont)+1)
dt = t[0:len(t):steps]

sin_t = numpy.sin(2 * numpy.pi * t * f0)
sin_dt = numpy.sin(2 * numpy.pi * dt * f0)

q_sin_t = quantize_midtread(sin_t, 2)
q_sin_dt = quantize_midtread(sin_dt, 2)

fig, (ax_sin1, ax_sin2) = pyplot.subplots(2, 1)
ax_sin1.plot(t, sin_t)
ax_sin1.plot(t, q_sin_t,'r') 
ax_sin1.set(xlabel='Zeit in s', ylabel='Amplitude', title='a) Nur Quantisierung (4 Stufen), Sinus = 100 Hz', xlim=[0, 0.02], ylim=[-1, 1])

ax_sin2.plot(t, sin_t)
markerline, stemlines, baseline = ax_sin2.stem(dt, q_sin_dt, use_line_collection=True, linefmt='r', markerfmt = 'or')
ax_sin2.set(xlabel='Zeit in s', ylabel='Amplitude', title='b) Abtastung (fs = 2000 Hz) + Quantisierung (4 Stufen), Sinus = 100 Hz', xlim=[0, 0.02], ylim=[-1, 1])
pyplot.tight_layout()

pyplot.show()

# glue this figure to paste it later (no effect outside of MyST NB)
from myst_nb import glue
glue("QuantisierungSinus", fig, display=False)
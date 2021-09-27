import matplotlib
import numpy
from matplotlib import pyplot

matplotlib.style.use('sv1_style.mplstyle')

def quantize_midrise (x, bits):
    input_midrise = numpy.linspace(-1 + (1/2**(bits-1)), 1, 2**bits)
    output_midrise = numpy.linspace(-1 + 2**-bits, 1 - (1/2**bits), 2**bits)
    quantized = [0]*len(x)
    for idx in range(len(x)-1):
        for n in range(len(input_midrise)):
            if x[idx] < input_midrise[n]:
                quantized[idx] = output_midrise[n]
                break
    return quantized
    
def quantize_midtread (x, bits):
    input_midtread = numpy.linspace(-1 + (1/2**bits), 1 - (1/2**bits), 2**bits)
    output_midtread = numpy.linspace(-1, 1 - (1/2**(bits-1)), 2**bits)
    for el in x:
        i = 0
        while el < input_midrise(i):
            i += 1
        el = output_midrise(i)

fs_cont = 100000
fs = 2000
f0 = 100
steps = int(fs_cont/fs)
T = 0.02
t = numpy.linspace(0, T, round(T*fs_cont)+1) # 0 to 0.02 s
dt = t[0:len(t):steps]

sin_t = numpy.sin(2 * 3.14 * t * f0)
sin_dt = numpy.sin(2 * 3.14 * dt * f0)

q_sin_t = quantize_midrise(sin_t, 4)
q_sin_dt = quantize_midrise(sin_dt, 4)


fig, (ax_sin1, ax_sin2) = pyplot.subplots(2, 1)
ax_sin1.plot(t, q_sin_t)
ax_sin1.step(dt, q_sin_dt, where='mid') # defines the steps of a step diagram
ax_sin1.set(xlabel='Zeit in s', ylabel='Amplitude', title='Nur Quantisierung (4 Stufen), Sinus = 100 Hz', xlim=[0, 0.02], ylim=[-1, 1])

ax_sin2.plot(t, q_sin_t)
markerline, stemlines, baseline = ax_sin2.stem(dt, q_sin_dt, use_line_collection=True)
ax_sin2.set(xlabel='Zeit in s', ylabel='Amplitude', title='b) Abtastung (fs = 2000 Hz) + Quantisierung (4 Stufen), Sinus = 100 Hz', xlim=[0, 0.02], ylim=[-1, 1])

pyplot.show()
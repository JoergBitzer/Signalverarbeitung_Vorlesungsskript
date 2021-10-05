import matplotlib
import numpy
from scipy import signal
from matplotlib import pyplot

matplotlib.style.use('sv1_style.mplstyle')

fig, ((ax_durch_b_c1, ax_durch_c2_c), (ax_sperr_b_c1, ax_sperr_c2_c), 
        (ax_phase_b_c1, ax_phase_c2_c)) = pyplot.subplots(3, 2)

f_s = 48000 

# filter design parameters
order = 4
Pass_freq = 0.1
Pass_dB = 0.2
Stop_freq = 0.2
Stop_dB = 30

# Filter design process: 
#   1. find necessary order for the desired parameters
#   2. use corresponding filter design function, 
#        giving the necessary parameter (not always all of them)
#   3. calculate the transfer function using freqz on the filter coefficients
# displaying:
#   4. show amplitude of transfer function in Pass stop and transition, 
#       using fitting zooms
#   5. show phase. numpy.unwrap for smooth display i.e. no jumps from 2*pi to 0

# Butterworth vs Chebychev-1 filter design
# ----------------------------------------

# Butterworth:
order, wn = signal.buttord(wp=Pass_freq, ws=Stop_freq, 
        gpass=Pass_dB, gstop=Stop_dB)
[b, a] = signal.butter(N=order, Wn=Pass_freq, output='ba')
[w, h] = signal.freqz(b, a)
w = w/numpy.pi

ax_durch_b_c1.plot(w, 20*numpy.log10(numpy.abs(h)))
ax_durch_b_c1.set(xlabel='Frequenz in rad/s', ylabel='Pegel in dB', 
        xlim=[0, 0.15], ylim=[-1, 0.2], title='a) Durchlassbereich')

ax_sperr_b_c1.plot(w, 20*numpy.log10(numpy.abs(h)))
ax_sperr_b_c1.set(xlabel='Frequenz in rad/s', ylabel='Pegel in dB', 
        xlim=[0.1, 1], ylim=[-80, -20], title='b) Sperrbereich')
ax_phase_b_c1.plot(w, numpy.unwrap(p=numpy.angle(h)))
ax_phase_b_c1.set(xlabel='Frequenz in rad/s', ylabel='Phase in rad', 
        xlim=[0, 1], title='c) Phase')

# Cheby1
order, wn = signal.cheb1ord(wp=Pass_freq, ws=Stop_freq, 
        gpass=Pass_dB, gstop=Stop_dB, fs=f_s)
[b, a] = signal.cheby1(N=order, rp=Pass_dB, Wn=Pass_freq, output='ba')
[w, h] = signal.freqz(b, a)
w = w/numpy.pi

ax_durch_b_c1.plot(w, 20*numpy.log10(numpy.abs(h)), linestyle='--')
ax_sperr_b_c1.plot(w, 20*numpy.log10(numpy.abs(h)), linestyle='--')
ax_phase_b_c1.plot(w, numpy.unwrap(p=numpy.angle(h)), linestyle='--')

# Chebychev-2 vs Cauer filter design
# ----------------------------------

# Cheby2
order, wn = signal.cheb2ord(wp=Pass_freq, ws=Stop_freq, 
        gpass=Pass_dB, gstop=Stop_dB, fs=f_s)
[b, a] = signal.cheby2(N=order, rs=Stop_dB, Wn=Stop_freq, output='ba')
[w, h] = signal.freqz(b, a)
w = w/numpy.pi

ax_durch_c2_c.plot(w, 20*numpy.log10(numpy.abs(h)))
ax_durch_c2_c.set(xlabel='Frequenz in rad/s', ylabel='Pegel in dB', 
        xlim=[0, 0.15], ylim=[-1, 0.2], title='d) Durchlassbereich')
ax_sperr_c2_c.plot(w, 20*numpy.log10(numpy.abs(h)))
ax_sperr_c2_c.set(xlabel='Frequenz in rad/s', ylabel='Pegel in dB', 
        xlim=[0.1, 1], ylim=[-80, -20], title='e) Sperrbereich')
ax_phase_c2_c.plot(w, numpy.unwrap(p=numpy.angle(h)))
ax_phase_c2_c.set(xlabel='Frequenz in rad/s', ylabel='Phase in rad', 
        xlim=[0, 1], title='f) Phase')

# Cauer
order, wn = signal.ellipord(wp=Pass_freq, ws=Stop_freq, 
        gpass=Pass_dB, gstop=Stop_dB, fs=f_s)
[b, a] = signal.ellip(N=order, rp=Pass_dB, rs=Stop_dB, 
        Wn=Pass_freq, output='ba')
[w, h] = signal.freqz(b, a)
w = w/numpy.pi

ax_durch_c2_c.plot(w, 20*numpy.log10(numpy.abs(h)), linestyle='--')
ax_sperr_c2_c.plot(w, 20*numpy.log10(numpy.abs(h)), linestyle='--')
ax_phase_c2_c.plot(w, numpy.unwrap(p=numpy.angle(h)),linestyle='--')

pyplot.tight_layout()
pyplot.show()
from scipy import signal
import matplotlib
from matplotlib import pyplot
import numpy

fig, (ax_hp, ax_bp, ax_bs) = pyplot.subplots(3, 1)
# HP
Pass_freq = 0.2
Pass_dB = 0.2
Stop_freq = 0.1
Stop_dB = 30
order, wn = signal.buttord(wp=Pass_freq, ws=Stop_freq, gpass=Pass_dB, gstop=Stop_dB)
[b, a] = signal.butter(N=order, Wn=Pass_freq, btype='highpass', output='ba')

[w, h] = signal.freqz(b, a)
w = w/numpy.pi
ax_hp.plot(w, 20*numpy.log10(numpy.abs(h)))

# BP
Pass_freqLow = 0.2
Pass_freqHigh = 0.3
Pass_dB = 0.2
Stop_freqLow = 0.1
Stop_freqHigh = 0.4
Stop_dB = 30
order, wn = signal.buttord(wp=Pass_freq, ws=Stop_freq, gpass=Pass_dB, gstop=Stop_dB)
[b, a] = signal.butter(N=order, Wn=[Pass_freqLow, Pass_freqHigh], btype='bandpass', output='ba')

[w, h] = signal.freqz(b, a)
w = w/numpy.pi
ax_bp.plot(w, 20*numpy.log10(numpy.abs(h)))

# BS
Pass_freqLow = 0.1
Pass_freqHigh = 0.4
Pass_dB = 0.2
Stop_freqLow = 0.2
Stop_freqHigh = 0.3
Stop_dB = 30 
order, wn = signal.buttord(wp=Pass_freq, ws=Stop_freq, gpass=Pass_dB, gstop=Stop_dB)
[b, a] = signal.butter(N=order, Wn=[Pass_freqLow, Pass_freqHigh], btype='bandstop', output='ba')

[w, h] = signal.freqz(b, a)
w = w/numpy.pi
ax_bs.plot(w, 20*numpy.log10(numpy.abs(h)))


pyplot.show()
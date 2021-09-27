import matplotlib
import soundfile
import numpy
from matplotlib import pyplot

matplotlib.style.use('sv1_style.mplstyle')

signal, samplerate = soundfile.read('Testsatz.wav') #reads signal and samplerate of the sound file
time = numpy.linspace(0, len(signal)/samplerate, len(signal)) # creates time vector in seconds

# Figure 1.1: cutting out a part of the signal

# setting start and end of the time
time_start = 1 # in seconds
time_end = 1.5 # in seconds

# cuts signal and time
sample_start = int(time_start * samplerate) # calculates the starting sample
sample_end = int(time_end * samplerate) # and the end sample
short_signal = signal[sample_start:sample_end] # cuts out the chosen timeframe from the signal 
short_time = time[sample_start:sample_end] # cuts the corresponding time vector

# plots
fig, ax = pyplot.subplots() # creates subplot
ax.plot(short_time, short_signal, label='Ausschnitt vom Sprachsignal', linewidth = 0.5)
ax.grid(axis='y', color='0.8')
ax.set(xlabel='Zeit in s', ylabel='Auslenkung (normalisiert auf 1)')
ax.spines['left'].set_visible(False)
ax.spines['right'].set_visible(False)
#ax.arrow(1, -0.68, 0.4, 0, head_width=0.05, head_length=0.1)

# displays
pyplot.show()
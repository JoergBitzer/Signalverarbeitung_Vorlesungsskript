import matplotlib
import soundfile
import numpy
from matplotlib import pyplot

# determine where we're running from and set paths accordingly
try: 
    if get_ipython().__class__.__name__ == 'ZMQInteractiveShell':
        prefix = ''
except:
    prefix = '../../'

matplotlib.style.use(f'{prefix}sv.mplstyle')

#reads signal and samplerate of the sound file
signal, samplerate = soundfile.read(f'{prefix}data/Testsatz.wav') 
# time vector in seconds
time = numpy.linspace(0, len(signal)/samplerate, len(signal)) 

# setting start and end of the time
time_start = 1 # in seconds
time_end = 1.5 # in seconds

# cuts signal and time
sample_start = int(time_start * samplerate) # calculates the starting sample
sample_end = int(time_end * samplerate) # and the end sample
short_signal = signal[sample_start:sample_end] # extracts the chosen timeframe 
short_time = time[sample_start:sample_end] # cuts the corresponding time vector

# plots
fig, ax = pyplot.subplots()
ax.plot(short_time, short_signal, label='Ausschnitt vom Sprachsignal', 
        linewidth = 0.5)
ax.grid(axis='y', color='0.8')
ax.set(xlabel='Zeit in s', ylabel='Auslenkung (normalisiert auf 1)')
ax.spines['left'].set_visible(False)
ax.spines['right'].set_visible(False)

pyplot.show()

# glue this figure to paste it later (no effect outside of MyST NB)
from myst_nb import glue
glue("sprachsignal", fig, display=False)
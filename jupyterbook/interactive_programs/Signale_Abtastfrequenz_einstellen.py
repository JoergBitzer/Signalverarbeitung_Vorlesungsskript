import matplotlib
import numpy
from matplotlib import pyplot
from matplotlib.widgets import Slider

matplotlib.style.use('../sv.mplstyle')

#'continous' sample is sampled as such a high frequency that it seem continuous
fs_cont = 100000 
fs = 1000 # discrete samplerate
freq = 200 # sinus frequency in Hz
steps = int(fs_cont/fs) # number of 'continuous' steps between discrete steps
T = 0.02 # signal length in s

# time vectors
t = numpy.linspace(0, T, T*fs_cont+1) # 'continuous'
dt = t[0:len(t):steps] # extracts discrete time from continuous time

# function values
sin_t = numpy.sin(2 * numpy.pi * t * freq) # continuous
sin_dt = numpy.sin(2 * numpy.pi * dt * freq) # discrete



# plots
fig_sin, ax_sin = pyplot.subplots()
pyplot.subplots_adjust(bottom=0.25)
ax_sin.plot(t, sin_t)
ax_sin.stem(dt, sin_dt, use_line_collection=True)
    
ax_sin.set_xlim([0, 0.02])
ax_sin.set(ylabel='Amplitude', xlabel='Zeit in s')
ax_sin.set_title(f'Sinus = {freq} Hz, Abtastfrequenz = {fs} Hz')

# adds slider for adjustable samplerate
ax_freq = pyplot.axes([0.25, 0.1, 0.65, 0.03], facecolor='lightgoldenrodyellow')
slider_freq = Slider(ax_freq, 
        'Abtastfrequenz (Hz)', 0, 3000, valinit=fs, valstep=10)

#updates the continuous and sampled values once the samplerate has been changed
def update(val):
    global fs
    ax_sin.cla()
    fs = slider_freq.val
    steps = int(fs_cont/fs)
    dt = t[0:len(t):steps]
    sin_dt = numpy.sin( 2 * numpy.pi * (freq * dt))
    ax_sin.plot(t, sin_t)
    ax_sin.stem(dt, sin_dt, use_line_collection=True)
    ax_sin.set_title(f'Sinusfrequenz = {freq} Hz, Abtastfrequenz = {fs}')
    fig_sin.canvas.draw_idle()

slider_freq.on_changed(update)

pyplot.show()

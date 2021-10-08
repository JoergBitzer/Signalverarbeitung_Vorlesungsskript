import matplotlib
import numpy
from matplotlib import pyplot
from matplotlib.widgets import Slider
from matplotlib.widgets import RadioButtons

matplotlib.style.use('../sv.mplstyle')

#'continous' sample is sampled as such a high frequency that it seem continuous
fs_cont = 100000 
fs = 1000 # discrete sampled
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
graph, = ax_sin.plot(t, sin_t)
markerline, stemlines, baseline = ax_sin.stem(
        dt, sin_dt, use_line_collection=True)
#stemlines.remove()

ax_sin.set_xlim([0, 0.02])
ax_sin.set(ylabel='Amplitude', xlabel='Zeit in s')
ax_sin.set_title(f'Sinus = {freq} Hz, Abtastfrequenz = 1000 Hz')

# adds slider for adjustable sinus frequency
ax_freq = pyplot.axes([0.45, 0.1, 0.45, 0.03], facecolor='lightgoldenrodyellow')
slider_freq = Slider(ax_freq, 
        'Sinusfrequenz (Hz)', 0, 3000, valinit=200, valstep=10)

# updates the continuous and sampled values once the frequency has been changed
def update(val):
    global freq
    ax_sin.cla()
    freq = slider_freq.val
    ax_sin.plot(t, numpy.sin( 2 * numpy.pi * (freq * t)))
    sin_dt = numpy.sin( 2 * numpy.pi * (freq * dt))
    ax_sin.stem(dt, sin_dt, use_line_collection=True)
    ax_sin.set_title(f'Sinusfrequenz = {freq} Hz, Abtastfrequenz = 1000 Hz')
    fig_sin.canvas.draw_idle()

slider_freq.on_changed(update)

pyplot.subplots_adjust(left=0.3)
rax = pyplot.axes([0.05, 0.7, 0.15, 0.15], facecolor='lightgoldenrodyellow')

radio = RadioButtons(rax, ('200 Hz', '800 Hz', '1200 Hz', '1800 Hz'))

def update_example(label):
    ax_sin.cla()
    hzdict = {'200 Hz': 200, '800 Hz': 800, '1200 Hz': 1200, '1800 Hz': 1800}
    freq = hzdict[label]
    ax_sin.plot(t, numpy.sin( 2 * numpy.pi * (freq * t)))
    sin_dt = numpy.sin( 2 * numpy.pi * (freq * dt))
    ax_sin.stem(dt, sin_dt, use_line_collection=True)
    ax_sin.set_title(f'Sinusfrequenz = {freq} Hz, Abtastfrequenz = 1000 Hz')
    fig_sin.canvas.draw_idle()
    
radio.on_clicked(update_example)

pyplot.show()
import matplotlib
import numpy
from matplotlib import pyplot
from matplotlib.widgets import Slider, RadioButtons

matplotlib.style.use('sv1_style.mplstyle')

def plot_noise():
    global count, bins, ignored    
    ax_noise.cla()
    
    if(noise_type=="gleich"):
        noise_data = numpy.random.uniform(low=x_min, high=x_max, size=noise_num)    
    else:
        noise_data = numpy.random.normal(mean, variance, noise_num)
    
    count, bins, ignored = ax_noise.hist(noise_data, stufen)
    fig_noise.canvas.draw_idle()

# rausch parameter
noise_num = 10000 # anzahl zufallswerte
amplitude = 10 
# parameter normalverteilung
mean = 0
variance = 1
# parameter gleichverteilung
x_min = -4 
x_max = 4
noise_type = "normal"
stufen = numpy.linspace(-10, 10, 41)

fig_noise, ax_noise = pyplot.subplots()
pyplot.subplots_adjust(left=0.25, bottom=0.25)

ax_noise.set_xlim([-10, 10])

uniform = numpy.random.uniform(low=x_min, high=x_max, size=noise_num)    
count, bins, ignored = ax_noise.hist(uniform, stufen)

# noise, = ax_noise.plot(noise_data , lw=1)

# fügt je einen slider für Mittelwert, Varianz der Normalverteilung und untere und obere Grenze der Gleichverteilung
axcolor = 'lightgoldenrodyellow'
ax_mean = pyplot.axes([0.25, 0.05, 0.65, 0.03], facecolor=axcolor)
ax_variance = pyplot.axes([0.1, 0.25, 0.03, 0.63], facecolor=axcolor)
ax_x_min = pyplot.axes([0.25, 0.10, 0.65, 0.03], facecolor=axcolor)
ax_x_max = pyplot.axes([0.25, 0.15, 0.65, 0.03], facecolor=axcolor)

# Definiert die möglichen Slidereinstellungen
slider_variance = Slider(ax_variance, 'Variance', 0.1, 10.0, valinit=variance, valstep=0.1, orientation='vertical')
slider_mean = Slider(ax_mean, 'Mean', -10.0, 10.0, valinit=mean, valstep=0.1, orientation='horizontal')
slider_x_min = Slider(ax_x_min, 'Min', -10.0, 1, valinit=x_min, valstep=0.1, orientation='horizontal')
slider_x_max = Slider(ax_x_max, 'Max', 1, 10, valinit=x_max, valstep=0.1, orientation='horizontal')

def update(val):
    '''
    Ändert die Rauschparameter wenn die Slider bewegt werden und updatet den plot
    '''
    global x_min, x_max, variance, mean # globale variablen außerhalb können verändert werden, wenn sie in der Funktion als global gekennzeichnet werden
    x_min = slider_x_min.val
    x_max = slider_x_max.val
    variance = slider_variance.val
    mean = slider_mean.val
    plot_noise()

# Bei Änderung aller Slider soll die Funktion "update" aufgerufen werden
slider_variance.on_changed(update)
slider_mean.on_changed(update)
slider_x_min.on_changed(update)
slider_x_max.on_changed(update)

# Fügt RadioButtons hinzu um den Rauschverteilungstyp umschalten zu können
radio_ax = pyplot.axes([0.025, 0.025, 0.15, 0.15], facecolor=axcolor)
radio = RadioButtons(radio_ax, ('gleich', 'normal'), active=0)

def change_noise_type(label):
    '''
    Ändert die rauschverteilung und updated den plot
    '''
    global noise_type
    noise_type = label
    plot_noise()
    
# Bei Änderung aller Slider soll die Funktion "change_noise_type" aufgerufen werden
radio.on_clicked(change_noise_type)

pyplot.show()
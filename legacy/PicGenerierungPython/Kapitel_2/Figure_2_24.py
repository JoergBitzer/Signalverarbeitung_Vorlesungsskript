import matplotlib
import numpy
from matplotlib import pyplot
from matplotlib.widgets import Slider, RadioButtons

matplotlib.style.use('sv1_style.mplstyle')

def plot_noise():
    '''
    helper function that changes the plot depending on existing variables
    '''
    global count, bins, ignored    
    ax_noise.cla()
    
    if(noise_type=="gleich"):
        noise_data = numpy.random.uniform(low=x_min, high=x_max,size=noise_num)    
    else:
        noise_data = numpy.random.normal(mean, variance, noise_num)
    
    count, bins, ignored = ax_noise.hist(noise_data, bin_steps)
    fig_noise.canvas.draw_idle()

# noise parameters
noise_num = 10000 # number of samples
amplitude = 10 
noise_type = "normal"

# parameter normal distribution
mean = 0
variance = 1
# parameters uniform distribution
x_min = -4 
x_max = 4

bin_steps = numpy.linspace(-10, 10, 41)

fig_noise, ax_noise = pyplot.subplots()
pyplot.subplots_adjust(left=0.25, bottom=0.25)

ax_noise.set_xlim([-10, 10])

uniform = numpy.random.uniform(low=x_min, high=x_max, size=noise_num)    
count, bins, ignored = ax_noise.hist(uniform, bin_steps)

# adds sliders mean and variance for normal distribuion
# and sliders for lower and upper bound used in the uniform distribution
axcolor = 'lightgoldenrodyellow'
ax_mean = pyplot.axes([0.25, 0.05, 0.65, 0.03], facecolor=axcolor)
ax_variance = pyplot.axes([0.1, 0.25, 0.03, 0.63], facecolor=axcolor)
ax_x_min = pyplot.axes([0.25, 0.10, 0.65, 0.03], facecolor=axcolor)
ax_x_max = pyplot.axes([0.25, 0.15, 0.65, 0.03], facecolor=axcolor)

# defines slider with scaling and appearance
slider_variance = Slider(ax_variance, 'Variance', 0.1, 10.0, 
        valinit=variance, valstep=0.1, orientation='vertical')
slider_mean = Slider(ax_mean, 'Mean', -10.0, 10.0, 
        valinit=mean, valstep=0.1, orientation='horizontal')
slider_x_min = Slider(ax_x_min, 'Min', -10.0, 1, 
        valinit=x_min, valstep=0.1, orientation='horizontal')
slider_x_max = Slider(ax_x_max, 'Max', 1, 10, 
        valinit=x_max, valstep=0.1, orientation='horizontal')

def update(val):
    '''
    refreshes all silder parameters

    Parameters:
    -----------
    val : float
        value of slider that is changed, probably unused
    '''
    # variables outside can be changed if they are declared as global
    global x_min, x_max, variance, mean 
    x_min = slider_x_min.val
    x_max = slider_x_max.val
    variance = slider_variance.val
    mean = slider_mean.val
    plot_noise()

# calls "update" for all sliders' movements
slider_variance.on_changed(update)
slider_mean.on_changed(update)
slider_x_min.on_changed(update)
slider_x_max.on_changed(update)

# Buttons for choosing the type of noise
radio_ax = pyplot.axes([0.025, 0.025, 0.15, 0.15], facecolor=axcolor)
radio = RadioButtons(radio_ax, ('gleich', 'normal'), active=0)

def change_noise_type(label):
    '''
    changes the displayed noise variable
    
    Parameters:
    -----------
    label : str
        button label, indicating noise type
    '''
    global noise_type
    noise_type = label
    plot_noise()
    
# call "change_noise_type" when radio button is clicked
radio.on_clicked(change_noise_type)

pyplot.show()
import matplotlib
import numpy
from matplotlib import pyplot
from matplotlib.widgets import RadioButtons

matplotlib.style.use('../sv.mplstyle')

current_light = "red" 
t = [0, 0.1, 0.2, 0.3] # initial times
# initial values to ensure the correct order of a stoplight in the plot
lights = ["green", "yellow", "red/yellow", "red"] 
d_t = 0.1 # Zeit nach einem Durchlauf in s
cur_t = 0.3

# Turns on the interactive mode of pyplot. 
# This allows for a change of the displayed data after opening the plot.
matplotlib.pyplot.ion() 
fig, ax = pyplot.subplots()
line, = ax.step(t, lights, where='post') # defines the steps of a step diagram
ax.grid(axis='x', color='0.8')
ax.set(xlabel='Zeit in s', ylabel='Ampelfarbe')
ax.set_xlim((0, 100))

fig.subplots_adjust(left=0.3)
rax = pyplot.axes([0.05, 0.15, 0.15, 0.75], facecolor='lightgoldenrodyellow')
radio = RadioButtons(rax, ('red', 'yellow', 'green'))

def lights_change(label):
    '''
    Handles the state change of stoplight color 
    according to the usual rules.
    
    Parameters:
    ---------------
    label : str
        button label, in this case color name
    '''
    
    global current_light
    
    if(label=='red' and current_light=='yellow'):
        current_light='red'
    elif(label=='yellow'):
        # yellow after green
        if(current_light=='green'):
            current_light='yellow'
        # red/yellow after red
        elif(current_light=='red'):
            current_light='red/yellow'
    elif(label=='green' and current_light=='red/yellow'):
        current_light='green'

# connects the function "lights_change" with the event of clicking one of the 
# radiobuttons. The function has to be implemented before this call
radio.on_clicked(lights_change)

pyplot.show()

# this loop run until the program is stopped
while(True):
    # appending to the vectors
    t = t + [cur_t]
    lights = lights + [current_light] 
    
    # update the displayed data
    line.set_xdata(t)
    line.set_ydata(lights)
    
    # wait a set time (30ms)
    cur_t += d_t
    pyplot.pause(d_t)
    
    ax.set(xlim=[cur_t-10, cur_t])

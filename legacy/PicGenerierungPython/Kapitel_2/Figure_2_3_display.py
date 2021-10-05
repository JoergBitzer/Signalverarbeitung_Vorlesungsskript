import matplotlib
import numpy
from matplotlib import pyplot
from matplotlib.widgets import RadioButtons
#import time

matplotlib.style.use('sv1_style.mplstyle')

d_t = 5 # Zeit nach einem Durchlauf in s

current_light = "red"
lights = ["green", "yellow", "yellow/red", "red", "red", "red", 
        "red", "yellow", "green", "green", "green"] 
t = numpy.linspace(0, d_t*(len(lights)-1), len(lights))
print(t)

fig, ax = pyplot.subplots()
line, = ax.step(t, lights, where='post') # defines the steps of a step diagram
ax.grid(axis='x', color='0.8')
ax.set(xlabel='Zeit in s', ylabel='Ampelfarbe')
ax.set_xlim((0, 50))

pyplot.show()
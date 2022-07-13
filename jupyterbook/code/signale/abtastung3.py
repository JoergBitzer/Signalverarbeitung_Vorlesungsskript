# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Demoscript for "Signalverarbeitung 1"
#
# Version: 1.0   17.02.2022
# 
# This software is released as public domain under CC0 1.0
# https://creativecommons.org/publicdomain/zero/1.0/
#-------------------------------------------------------------------------------

import matplotlib
import numpy
from matplotlib import pyplot
from matplotlib.widgets import Slider
from matplotlib.widgets import RadioButtons


def isnotebook(): 
#from https://stackoverflow.com/questions/15411967/how-can-i-check-if-code-is-executed-in-the-ipython-notebook
    try:
        shell = get_ipython().__class__.__name__
        if shell == 'ZMQInteractiveShell':
            return True   # Jupyter notebook or qtconsole
        elif shell == 'TerminalInteractiveShell':
            return False  # Terminal running IPython
        else:
            return False  # Other type (?)
    except NameError:
        return False      # Probably standard Python interpreter



nbflag = isnotebook()
# nbflag = True

if (nbflag == False):

    fs_cont = 100000 # 'continous' sample is sampled as such a high frequency that it seem continuous
    fs = 1000 # discrete sampled
    freq = 100 # sinus frequency in Hz
    steps = int(fs_cont/fs) # number of 'continuous' steps between discrete steps
    T = 0.04 # signal length in s

    # time vectors
    t = numpy.linspace(0, T, int(T*fs_cont+1)) # 'continuous'
    dt = t[0:len(t):steps] # extracts discrete time from continuous time

    # function values
    sin_t = numpy.sin(2 * numpy.pi * t * freq) # continuous
    sin_dt = numpy.sin(2 * numpy.pi * dt * freq) # discrete

    # plots
    fig_sin, ax_sin = pyplot.subplots()
    pyplot.subplots_adjust(bottom=0.25)
    graph, = ax_sin.plot(t, sin_t)
    markerline, stemlines, baseline = ax_sin.stem(dt, sin_dt, use_line_collection=True, linefmt='r', markerfmt = 'or')
    #stemlines.remove()

    ax_sin.set_xlim([0, 0.03])
    ax_sin.set(ylabel='Amplitude', xlabel='Zeit in s')
    ax_sin.set_title(f'Sinus = 100 Hz, Abtastfrequenz = {fs} Hz')

    # adds slider for adjustable sinus frequency
    ax_freq = pyplot.axes([0.45, 0.1, 0.45, 0.03], facecolor='lightgoldenrodyellow')
    slider_freq = Slider(ax_freq, 'Sinusfrequenz (Hz)', 0, 2000, valinit=fs, valstep=10)

    # updates the continuous and sampled values once the frequency has been changed
    def update(val):
        global freq
        ax_sin.cla()
        fs = slider_freq.val
        steps = int(fs_cont/fs) # number of 'continuous' steps between discrete steps

        # time vectors
        t = numpy.linspace(0, T, int(T*fs_cont+1)) # 'continuous'
        dt = t[0:len(t):steps] # extracts discrete time from continuous time
        
        ax_sin.plot(t, numpy.sin( 2 * numpy.pi * (freq * t)))
        sin_dt = numpy.sin( 2 * numpy.pi * (freq * dt))
        ax_sin.stem(dt, sin_dt, use_line_collection=True,linefmt='r', markerfmt = 'or')
        ax_sin.set_title(f'Sinusfrequenz = 100 Hz, Abtastfrequenz = {fs} Hz')
        fig_sin.canvas.draw_idle()

    slider_freq.on_changed(update)

    pyplot.subplots_adjust(left=0.3)
    rax = pyplot.axes([0.05, 0.7, 0.15, 0.15], facecolor='lightgoldenrodyellow')

    radio = RadioButtons(rax, ('100 Hz', '200 Hz', '300 Hz', '500 Hz', '1000 Hz'))

    def update_example(label):
        ax_sin.cla()
        hzdict = {'100 Hz': 100, '200 Hz': 200, '300 Hz': 300, '500 Hz': 500, '1000 Hz': 1000}
        fs = hzdict[label]
        steps = int(fs_cont/fs) # number of 'continuous' steps between discrete steps
        
        # time vectors
        t = numpy.linspace(0, T, int(T*fs_cont+1)) # 'continuous'
        dt = t[0:len(t):steps] # extracts discrete time from continuous time

        ax_sin.plot(t, numpy.sin( 2 * numpy.pi * (freq * t)))
        sin_dt = numpy.sin( 2 * numpy.pi * (freq * dt))
        ax_sin.stem(dt, sin_dt, use_line_collection=True, linefmt='r', markerfmt = 'or')
        ax_sin.set_title(f'Sinusfrequenz = 100 Hz, Abtastfrequenz = {fs} Hz')
        fig_sin.canvas.draw_idle()
        slider_freq.set_val(fs)
        
    radio.on_clicked(update_example)
    pyplot.show()
else:
    # matplotlib.style.use('sv.mplstyle')
    fs_cont = 100000 # 'continous' sample is sampled as such a high frequency that it seem continuous
    fs = [1000, 500, 300, 200, 150, 100] # discrete sampled
    freq = [100] # sinus frequency in Hz
    alpha = ['a) ','b) ','c) ','d) ','e) ','f) ']
    T = 0.04 # signal length in s

    fig_sin, ax_sin = pyplot.subplots(nrows=3, ncols=2)
    
    for count,ff in enumerate(fs):
    # time vectors
        steps = int(fs_cont/ff) # number of 'continuous' steps between discrete steps
        t = numpy.linspace(0, T, int(T*fs_cont+1)) # 'continuous'
        dt = t[0:len(t):steps] # extracts discrete time from continuous time
    # function values
        sin_t = numpy.sin(2 * numpy.pi * t * freq) # continuous
        sin_dt = numpy.sin(2 * numpy.pi * dt * freq) # discrete
        if (count == 0):
            ax = ax_sin[0][0]
        
        if (count == 1):
            ax = ax_sin[0][1]
        
        if (count == 2):
            ax = ax_sin[1][0]
        
        if (count == 3):
            ax = ax_sin[1][1]

        if (count == 4):
            ax = ax_sin[2][0]
        
        if (count == 5):
            ax = ax_sin[2][1]
        
        graph, = ax.plot(1000*t, sin_t)
        markerline, stemlines, baseline = ax.stem(1000*dt, sin_dt, use_line_collection=True, linefmt='r', markerfmt = 'or')
    #stemlines.remove()

        ax.set_xlim([0, 30])
        ax.set(ylabel='Amplitude', xlabel='Zeit in ms')
    
        fig_name = alpha[count]
        ax.set_title(f'{fig_name}Sinus = 100 Hz, Abtastfrequenz = {ff} Hz')

    pyplot.tight_layout()
    pyplot.show()

# glue this figure to paste it later (no effect outside of MyST NB)
from myst_nb import glue
glue("Abtast3", fig_sin, display=False)    
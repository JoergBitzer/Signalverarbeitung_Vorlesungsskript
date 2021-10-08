import matplotlib
import numpy
from matplotlib import pyplot

matplotlib.style.use('../sv.mplstyle')

def impulse(num_samples, pole):
    '''
    Parameters:
    -----------
    num_samples : int
        length of impulse
    pole : array
        complex pole
    '''
    r_pole = (pole.real**2 + pole.imag**2)**0.5 # radius of pole
    phi_pole = numpy.angle(pole) # angle of pole
    
    A = -1j*(numpy.exp(1j*phi_pole))/(2*numpy.sin(phi_pole))
    r_A = numpy.abs(A)
    phi_A = numpy.angle(A)
    y = numpy.zeros(num_samples)
    for idx in range(num_samples):
        y[idx] = 2 * r_A * r_pole**idx * numpy.cos(phi_pole*idx + phi_A)
    return y

def onclick(event):
    '''
    
    Parameters:
    -----------
    event : Event
        event of the mouse click with information of interest
    '''
    
    ax_pz.lines[1].remove() # deletes pole
    ax_imp.cla()
    
    # translating position in graph to complex number
    pole = event.xdata + 1j*event.ydata
    y = impulse(50, pole) # create impulse response of length 50
    
    ax_pz.plot([pole.real, pole.real], [pole.imag, -pole.imag], 
            marker='X', linestyle='none', color='blue')
    ax_imp.stem(y, use_line_collection=True)
    ax_imp.set(xlabel='Folgenkindex k ->', ylabel='Amplitude', 
            title=f'Impulsantwort des Systems', 
            xlim=[0, num_samples-1], ylim=[-y.max(), y.max()])
    fig.canvas.draw_idle()


# create circle with anglual resulution vector theta
theta = numpy.linspace(0, 2*numpy.pi, 100)
circle = numpy.exp(1j*theta)
pole = 1+0j

num_samples = 50
y = impulse(num_samples, pole)

fig, (ax_pz, ax_imp) = pyplot.subplots(1, 2)

# Pole-Zero Plot
ax_pz.plot(circle.real, circle.imag)
ax_pz.plot([pole.real, pole.real], [pole.imag, -pole.imag], 
        marker='X', linestyle='none', color='blue')
ax_pz.set(xlabel=r'Realteil', ylabel=r'Imaginärteil', 
        title='Pol-Nullstellen-Plan', xlim=[-1.5, 1.5], ylim=[-1.5, 1.5])

# Impulse Plot
ax_imp.stem(y, use_line_collection=True)
ax_imp.set(xlabel='Folgenkindex k ->', ylabel='Amplitude', 
        title='Impulsantwort des Systems', xlim=[0, num_samples-1])

cid = fig.canvas.mpl_connect('button_press_event', onclick)
pyplot.show()
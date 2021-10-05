import matplotlib
import numpy
from matplotlib import pyplot

matplotlib.style.use('sv1_style.mplstyle')

index_causal = numpy.linspace(-10, 10, 21)
amplitude_causal = [0]*len(index_causal)
mid_causal = int(numpy.floor(len(index_causal)/2))
for idx in range(len(index_causal)-mid_causal):
    # arbitrary causal function
    amplitude_causal[idx+mid_causal] = 0.5**idx

fig, (ax_causal, ax_ncausal) = pyplot.subplots(1, 2)
ax_causal.stem(index_causal, amplitude_causal, use_line_collection=True)
ax_causal.set(xlabel='Folgenkindex k ->', ylabel='Amplitude x(k)', 
        title='kaulase Folge 0.5**(k)*gamma(k)', xlim=[-10, 10])

index_ncausal = numpy.linspace(-10, 10, 21)
amplitude_ncausal = [0]*len(index_ncausal)
mid_ncausal = int(numpy.floor(len(index_ncausal)/2))
for idx in range(len(index_ncausal)-mid_ncausal):
    # arbitrary non-causal function
    amplitude_ncausal[idx] = -1 * 0.5**(-10+idx)

ax_ncausal.stem(index_ncausal, amplitude_ncausal, use_line_collection=True)
ax_ncausal.set(xlabel='Folgenkindex k ->', ylabel='Amplitude x(k)', 
        title='nicht causale Folge -0.5**(-k)*gamma(-k)', 
        xlim=[-10, 10], ylim=[-50, 0])

pyplot.show()
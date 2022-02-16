import matplotlib
import numpy
from matplotlib import pyplot

# determine where we're running from and set paths accordingly
try: 
    if get_ipython().__class__.__name__ == 'ZMQInteractiveShell':
        prefix = ''
except:
    prefix = '../../'

matplotlib.style.use(f'{prefix}sv.mplstyle')

index_kausal = numpy.linspace(-10, 10, 21)
amplitude_kausal = [0]*len(index_kausal)
mid_kausal = int(numpy.floor(len(index_kausal)/2))
for idx in range(len(index_kausal)-mid_kausal):
    amplitude_kausal[idx+mid_kausal] = 0.5**idx

fig, (ax_kausal, ax_nkausal) = pyplot.subplots(1, 2)
ax_kausal.stem(index_kausal, amplitude_kausal, use_line_collection=True)
ax_kausal.set(xlabel='Folgenkindex k ->', ylabel='Amplitude x(k)', title='kausale Folge 0.5**(k)*gamma(k)', xlim=[-10, 10])

index_nkausal = numpy.linspace(-10, 10, 21)
amplitude_nkausal = [0]*len(index_nkausal)
mid_nkausal = int(numpy.floor(len(index_nkausal)/2))
for idx in range(len(index_nkausal)-mid_nkausal):
    amplitude_nkausal[idx] = -1 * 0.5**(-10+idx)

ax_nkausal.stem(index_nkausal, amplitude_nkausal, use_line_collection=True)
ax_nkausal.set(xlabel='Folgenkindex k ->', ylabel='Amplitude x(k)', title='nicht kausale Folge -0.5**(-k)*gamma(-k)', xlim=[-10, 10], ylim=[-50, 0])

pyplot.show()

# glue this figure to paste it later (no effect outside of MyST NB)
from myst_nb import glue
glue("zFolgenPic", fig, display=False)
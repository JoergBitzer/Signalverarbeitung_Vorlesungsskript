import matplotlib
from matplotlib import pyplot

matplotlib.style.use('sv1_style.mplstyle')
fig, ax_Fx = pyplot.subplots()
ax_Fx.step(x=[-2, 1, 2, 3, 4, 5, 6, 10], y=[0, 0, 1/6, 2/6, 3/6, 4/6, 5/6, 1], color='b')

ax_Fx.set(xlabel='x -> ', ylabel='F(x)', xlim=[-1, 8], ylim=[-0.1, 1.1])

pyplot.show()
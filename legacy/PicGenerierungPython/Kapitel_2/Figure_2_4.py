import matplotlib
import numpy
from matplotlib import pyplot

matplotlib.style.use('sv1_style.mplstyle')

len_cont = 1100 # number of steps for continuous signal
len_disc = 11 # number of steps for discrete signal
# number of 'continuous' steps between discrete steps
steps = int(len_cont/len_disc) 

t = numpy.linspace(0, 11, len_cont) # 'continuously' sampled
dt = numpy.linspace(0, 11, len_disc) # discretely sampled
v = 0.05*(t-1)*(t-4)*(t-9) # example cubic function values
dv = numpy.round(v[:]) # discrete values of function rounded to integers
v_dt = v[0 : (len_cont+steps) : steps] #discretely sampled, non discrete values 
dv_dt = dv[0 : (len_cont+steps) : steps] # discretely sampled, discrete values

# abbreviations: ct/cv = continuous time/values, dt/dv = discrete time/values
fig, ((ax_2x2_ct_cv, ax_2x2_dt_cv), 
        (ax_2x2_ct_dv, ax_2x2_dt_dv)) = pyplot.subplots(2, 2)

ax_2x2_ct_cv.plot(t, v)
ax_2x2_ct_dv.plot(t, dv)
ax_2x2_dt_cv.stem(dt, v_dt, use_line_collection=True)
ax_2x2_dt_dv.stem(dt, dv_dt, use_line_collection=True)

ax_2x2_ct_cv.set(xlabel='Zeit in s', ylabel='Ausgangswerte', 
        title='zeit- und wertkontinuierlich (analog)')
ax_2x2_dt_cv.set(xlabel='Zeit (diskret) in s', ylabel='Ausgangswerte', 
        title='zeitdiskret und wertkontinuierlich')
ax_2x2_ct_dv.set(xlabel='Zeit in s', ylabel='Ausgangswerte (diskret)', 
        title='zeitkontinuerlich und wertdiskret')
ax_2x2_dt_dv.set(xlabel='Zeit (diskret) in s',ylabel='Ausgangswerte (diskret)', 
        title='zeit- und wertdikret (digital)')
pyplot.tight_layout()
pyplot.show()
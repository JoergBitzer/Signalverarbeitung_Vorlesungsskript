# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Demoscript for "Signalverarbeitung 1"
#
# Version: 1.0   17.02.2022
# 
# This software is released as public domain under CC0 1.0
# https://creativecommons.org/publicdomain/zero/1.0/
#-------------------------------------------------------------------------------

#%matplotlib inline
import time
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal
import ipywidgets as widgets
from IPython.display import display

radius_poles = 0.9
omega_poles = np.pi / 10

pole_list = [radius_poles * np.exp(1j*omega_poles)]
pole_list.append(pole_list[0].conjugate())


radius_zeros = 0.95
omega_zeros = 7 * np.pi / 10

zero_list = [radius_zeros * np.exp(1j*omega_zeros)]
zero_list.append(zero_list[0].conjugate())


# from poles and zeros, compute system coefficients
a_coefficients = np.poly(pole_list)
b_coefficients = np.poly(zero_list)

# draw poles and zeros
#plt.figure(1)
#plt.scatter(np.real(pole_list), np.imag(pole_list), marker='x', c='r')
#plt.scatter(np.real(zero_list), np.imag(zero_list), marker='o', c='b')

# draw unit circle inside the same plot
angles_rad = np.linspace(0, 2*np.pi, 512)
#plt.plot(np.cos(angles_rad), np.sin(angles_rad), c='k')

# plot formatting stuff
#plt.axis('equal')
#plt.grid()
#plt.title('Pol-Nullstellen-Plan')
#plt.xlabel('Re(z)')
#plt.ylabel('Im(z)')
#plt.show()
# compute complex-valued transfer function
_, transfer_function = signal.freqz(b_coefficients, a_coefficients, whole=True)


# def pole_zero_influence_plot(spec_idx):
    
fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(15, 5))

# first subplot: pole-zero plot
ax[0].scatter(np.real(pole_list), np.imag(pole_list), marker='x', c='r')
ax[0].scatter(np.real(zero_list), np.imag(zero_list), marker='o', c='b')
ax[0].plot(np.cos(angles_rad), np.sin(angles_rad), c='k')
ax[0].set(aspect='equal')

# second subplot: magnitude of transfer function
ax[1].plot(20*np.log10(np.abs(transfer_function)))
ax[1].set_xlim([0, len(transfer_function)])
ax[1].set_ylim([-40, 40])

# second subplot: phase of transfer function
ax[2].plot(np.angle(transfer_function))
ax[2].set_xlim([0, len(transfer_function)])

ax[2].set_ylim([-np.pi, np.pi])

# draw lines from each pole to the current index
#or pole_idx in range(0, len(pole_list)):
#   ax[0].plot([np.cos(angles_rad[spec_idx]), np.real(pole_list[pole_idx])],
#              [np.sin(angles_rad[spec_idx]), np.imag(pole_list[pole_idx])], ':')

# draw lines from each zero to the current index
#or zero_idx in range(0, len(zero_list)):
#   ax[0].plot([np.cos(angles_rad[spec_idx]), np.real(zero_list[zero_idx])],
#              [np.sin(angles_rad[spec_idx]), np.imag(zero_list[zero_idx])], ':')

# plot markers into transfer function plots at the same index
#x[1].plot([spec_idx, spec_idx], [-40, 20*np.log10(np.abs(transfer_function[spec_idx]))])
#x[2].plot([spec_idx, spec_idx], [-np.pi, np.angle(transfer_function[spec_idx])])

        

# create a slider that uses the slider value inside of the plot function
# interactive_plot = widgets.interactive(pole_zero_influence_plot, spec_idx=(1, len(transfer_function)-1, 5))

# show the slider and the plot
# interactive_plot
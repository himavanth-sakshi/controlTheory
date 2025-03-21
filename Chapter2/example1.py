'''
Q1) Find the transfer function of an RC circuit (low-pass filter) and plot its Bode plot.
'''


import numpy as np
import matplotlib.pyplot as plt
import control as ctrl

# Given values
R = 10e3  # 10 kΩ
C = 10e-6  # 10 μF

# Transfer function G(s) = 1 / (RCs + 1)
num = [1]
den = [R * C, 1]
G = ctrl.TransferFunction(num, den)

# Plot Bode plot
plt.figure()
ctrl.bode_plot(G, dB=True)
plt.show()

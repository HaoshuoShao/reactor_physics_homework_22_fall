import numpy as np
import matplotlib.pyplot as plt
import math
import pylab

def J_0(x):
    return 1 - (x**2)/4 + (x**4)/64 - (x**6)/2304

def J_1(x):
    return x/2 - (x**3)/16 + (x**6)/384

R = 0.1634
Z = 0.375

r = np.linspace(0, R, 50, endpoint=True)

phi = J_0(2.405*r/R)

z = np.linspace(0, Z, 50, endpoint=True)
phi = np.sin(3.1416*z/Z)

plt.plot(z, phi)

plt.show()
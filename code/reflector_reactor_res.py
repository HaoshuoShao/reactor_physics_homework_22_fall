import numpy as np
import matplotlib.pyplot as plt
import scipy.special as spec

K_INFTY = 2.026
M2 = 0.0040673
PI = 3.1416
L_R2 = 0.09706
D_R = 0.007086
D_C = 0.001301


def J_0(x):
    return spec.jn(0, x)

def J_1(x):
    return spec.jn(1, x)

def I_0(x):
    return spec.iv(0, x)

def I_1(x):
    return spec.iv(1, x)

def K_0(x):
    return spec.kv(0, x)

def K_1(x):
    return spec.kv(1, x)

def B_r(h):
    return ((K_INFTY-1)/M2 - (PI/h)**2)**0.5

def bar_K_r2(h):
    return 1/L_R2+(PI/h)**2

def equleft(r, h):
    h = h + 0.025
    Br = B_r(h)
    kr_bar = bar_K_r2(h)**0.5
    left = Br*J_1(Br*r)/J_0(Br*r)
    return left

def equright(r, h):
    h = h + 0.025
    kr_bar = bar_K_r2(h)**0.5
    right = kr_bar*D_R/D_C*K_1(kr_bar*r)/K_0(kr_bar*r)
    return right

r = np.linspace(0.12, 0.17, 100, endpoint=True)
left = equleft(r, 0.375)
right = equright(r, 0.375)

plt.plot(r, left, color = 'red')
plt.plot(r, right, color = 'blue')

plt.show()
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
    Br = B_r(h)
    left = Br*J_1(Br*r)/J_0(Br*r)
    return left

def equright(r, h):
    kr_bar = bar_K_r2(h)**0.5
    right = kr_bar*D_R/D_C*K_1(kr_bar*r)/K_0(kr_bar*r)
    return right

def psi_c(r, H):
    Br = B_r(H)
    return J_0(Br*r)

def psi_r(r, H):
    kr_bar = bar_K_r2(H)**0.5
    return K_0(kr_bar*r)

def psi_func(r, R_c, H):
    c1 = 1/psi_c(0, H)
    c2 = c1*psi_c(R_c, H)/psi_r(R_c, H)

    if r < R_c:
        return c1*psi_c(r, H)
    
    else:
        return c2*psi_r(r, H)

# 带反射层的中子通量密度分布
R = 0.1574
H = 0.4
r = np.linspace(0, 1.5*R, 100, endpoint=True)

psi = np.linspace(0, 1.5*R, 100, endpoint=True)

for i in range(100):
    x = float(r[i])
    psi[i] = psi_func(x, R, H)

plt.plot(r, psi, color = 'red')

# 裸堆的中子通量密度分布
R_b = 0.1634
H_b = 0.375
r_b = np.linspace(0, R_b, 100, endpoint=True)

psi_b = J_0(2.405*r_b/R_b)

plt.plot(r_b, psi_b, color = 'blue')

plt.show()
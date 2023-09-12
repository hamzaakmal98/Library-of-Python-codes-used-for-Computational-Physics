# psi (x) =  Ae^ikx + Be^-ikx for x>0
# psi(x) = Ce^ikx for x< 0
# psi(x) = A(e^ikx + B/Ae^−ikx)
# psi (x) = A(C/A e^-k')
#
# d^2psi/ dx = A(k'^2 * C/A e^-k')
#
# Kinetic Energy - T = -1/2psi(x) * d^2psi/ dx
#
# Therefore, for k = 2 and k' = 4 for x > 0 and x< 0 respectively
#
# T = 2
# T = -8

import cmath
import numpy as np
import matplotlib.pyplot as plt

B_A = 2 / (1 + 1j * 2)
C_A = (1 - 1j * 2) / (1 + 1j * 2)


def finiteWell(x):
    y = np.zeros_like(x, dtype=np.complex128)
    y[x < 0] = np.exp((1j * 2 * x[x < 0])) + B_A * np.exp(-1j * 2 * x[x < 0])
    y[x > 0] = C_A * np.exp(-4 * x[x > 0])
    return y


def kinetic(f_x, x, h):
    psiold = f_x(x)
    psi_p = f_x(x + h)
    psi_m = f_x(x - h)

    laplacian = (psi_p + psi_m - 2. * psiold) / h ** 2
    return -0.5 * laplacian / psiold


x = np.arange(-10, -0.1, 0.001)
plt.plot(x, finiteWell(x))
plt.show()
kinetic(finiteWell, 5, 0.0005).real

#I'm getting a weird error at the end. The graph prints correctly but there's something happening that I cant fix :(

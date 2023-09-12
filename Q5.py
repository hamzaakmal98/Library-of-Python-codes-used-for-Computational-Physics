# The second derivative of Psi with respect to x is calculated here using the central difference method appropriated
# to the second derivative. The first derivative is calculated by using the approximation psi'(x) = (psi(x+h) - psi(
# x-h))/h where h is the small interval we have chosen for the calculation. It is important to have a small value of
# h to ensure that we take small step sizes during our iteration This ensures that the 'gaps' left by the trapezoid
# rule of calculation are minimized and the function is as close to the actual value as possible. For the second
# derivative, the taylor expansion of the function psi is elaborated and truncated after the order of O(psi'''")
# The formula for central difference of the first derivative is then substituted into the formula and the required
# expression is derived as shown in the working.
import numpy as np
import math
import matplotlib.pyplot as plt

m = 1
w = 1
hbar = 1

def psi_n(x, n):
    prefactor = 1/math.sqrt(2**n * math.factorial(n)) * (m*w/math.pi/hbar)**0.25
    hermite = np.polynomial.hermite.Hermite(n)(math.sqrt(m*w/hbar)*x)
    return prefactor * np.exp(-m*w*x**2/2/hbar) * hermite

def psi_squared(x, n):
    return np.abs(psi_n(x, n))**2

def classical(x):
    return np.exp(-m*w*x**2/2/hbar)

x_min = -5
x_max = 5
num_points = 1000
x = np.linspace(x_min, x_max, num_points)

fig, ax = plt.subplots(figsize=(10, 8))
ax.set_xlabel('Position (x)')
ax.set_ylabel('Probability density')
ax.set_title('Quantum harmonic oscillator eigenfunctions squared and classical solution')

for n in range(0, 5):
    psi_squared_n = psi_squared(x, n)
    ax.plot(x, psi_squared_n, label=f"n={n}")
ax.plot(x, classical(x), 'k-', label='Classical solution')
ax.legend()
ax.set_ylim(0, 1.2)

plt.show()

import cmath
import math

#Boundary conditions follow from the discretization of intervals at the beginning of the algorithm. This made
# subsequent calculations smooth because terms that were truncated contributed to possible discontinuities.

# #TIME OUT SO STOPPED HERE, NEED TO PLOT THIS AS WELLL ON THE GRAPH. ENERGIES ARE EASILY CALCULATED FROM THIS
# def psibox(x, cardinal_num, boxl):
#
#     k = 2 * math.pi / L * cmath.sqrt(nx ** 2 )
#     return cmath.exp(1j * k * x)
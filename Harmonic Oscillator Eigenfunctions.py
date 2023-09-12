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

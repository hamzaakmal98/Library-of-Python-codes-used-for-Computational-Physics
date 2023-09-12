import numpy as np
import scipy.integrate as spi
from scipy.special import hermite

def harmonic_oscillator(x, y, z, nx, ny, nz, w):
    """Returns the value of the wave function for the 3D harmonic oscillator
    with different quantum numbers nx, ny, nz in the x, y, z Cartesian components,
    and frequency w.
    """
    psi_x = hermite(nx)(np.sqrt(w)*x) * np.exp(-w*x**2/2)
    psi_y = hermite(ny)(np.sqrt(w)*y) * np.exp(-w*y**2/2)
    psi_z = hermite(nz)(np.sqrt(w)*z) * np.exp(-w*z**2/2)
    return psi_x * psi_y * psi_z

def kinetic(psi, dx, dy, dz):
    """Returns the kinetic energy of a wave function psi on a 3D grid
    with grid spacing dx, dy, dz.
    """
    psi_x = np.roll(psi, 1, axis=0) + np.roll(psi, -1, axis=0) - 2 * psi
    psi_y = np.roll(psi, 1, axis=1) + np.roll(psi, -1, axis=1) - 2 * psi
    psi_z = np.roll(psi, 1, axis=2) + np.roll(psi, -1, axis=2) - 2 * psi
    return -0.5 * (psi_x/dx**2 + psi_y/dy**2 + psi_z/dz**2).sum()

def psiqho(nx, ny, nz, w, x, y, z):
    """Returns the value of the wave function for the 3D harmonic oscillator
    with different quantum numbers nx, ny, nz in the x, y, z Cartesian components,
    and frequency w.
    """
    return harmonic_oscillator(x, y, z, nx, ny, nz, w)

# Set up the grid
N = 51
x = np.linspace(-5, 5, N)
y = np.linspace(-5, 5, N)
z = np.linspace(-5, 5, N)
dx = x[1] - x[0]
dy = y[1] - y[0]
dz = z[1] - z[0]
X, Y, Z = np.meshgrid(x, y, z, indexing='ij')

# Set up the quantum numbers and frequency
nx = 1
ny = 2
nz = 3
w = 1.0

# Calculate the wave function and its kinetic energy
psi = psiqho(nx, ny, nz, w, X, Y, Z)
T = kinetic(psi, dx, dy, dz)

# Calculate the total energy
V = 0.5 * w**2 * (X**2 + Y**2 + Z**2)
E = (T + V).sum() * dx * dy * dz

print("Quantum numbers: nx = %d, ny = %d, nz = %d" % (nx, ny, nz))
print("Frequency: w = %.2f" % w)
print("Total energy: E = %.2f" % E)

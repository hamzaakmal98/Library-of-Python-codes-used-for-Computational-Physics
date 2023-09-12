import numpy as np
import matplotlib.pyplot as plt

def DFT(x):
    """Compute the discrete Fourier Transform of the 1D array x"""
    N = x.size
    n = np.arange(N)
    k = n.reshape((N, 1))
    M = np.exp(-2j * np.pi * k * n / N)
    return np.dot(M, x)

# Define the function f(x)
w = 2*np.pi/10
x = np.linspace(0, 10, 1000)
f = np.sin(w*x) + np.cos(w*x)

# Compute the DFT of f(x)
F = DFT(f)

# Plot the results
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6))

ax1.plot(x, f, color='blue')
ax1.set_xlabel('x')
ax1.set_ylabel('f(x)')
ax1.set_title('Function f(x) = sin(wx) + cos(wx)')

ax2.plot(np.abs(F), color='red')
ax2.set_xlabel('k')
ax2.set_ylabel('|F(k)|')
ax2.set_title('DFT of f(x)')

plt.tight_layout()
plt.show()

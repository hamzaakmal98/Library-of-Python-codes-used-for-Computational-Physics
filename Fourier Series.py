import numpy as np
from sympy import *

# Define the function to find the Fourier series expansion of
x = symbols('x')
f = 1 - x**2

# Define the range of the Fourier series
L = pi
n_max = 5

# Define the coefficients of the Fourier series
a_0 = (1/L) * integrate(f, (x, -L, L))
a_n = lambda n: (1/L) * integrate(f*cos(n*x), (x, -L, L))
b_n = lambda n: (1/L) * integrate(f*sin(n*x), (x, -L, L))

# Compute the Fourier series expansion
fourier_series = a_0/2
for n in range(1, n_max+1):
    fourier_series += a_n(n)*cos(n*x) + b_n(n)*sin(n*x)

# Print the Fourier series expansion
print("Fourier series expansion of", f, "for n =", n_max)
print(fourier_series)

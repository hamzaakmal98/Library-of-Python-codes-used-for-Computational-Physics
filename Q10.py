import numpy as np
import matplotlib.pyplot as plt


def square_wave(x):
    return 0.5 - np.floor(x / np.pi) % 2


def fourier_coefficient(n):
    if n == 0:
        return 0.0

    elif n % 2 == 0:
        return 0.0

    else:
        m = (n - 1) // 2
        return (-1) ** m / (np.pi * n)


def fourier_series(x, nmax):
    result = 0.0

    for n in range(1, nmax + 1):
        coefficient = fourier_coefficient(n)
        term = coefficient * np.sin(n * x)
        result += term

    return result


x = np.linspace(-np.pi, np.pi, 1000)
nmax_values = [1, 3, 5, 7, 9, 21, 51, 100]

plt.figure(figsize=(12, 8))
plt.plot(x, square_wave(x), 'k-', label='Square Wave')
for nmax in nmax_values:
    plt.plot(x, fourier_series(x, nmax), label=f'nmax={nmax}')

plt.legend()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Square Wave and Fourier Series')

plt.show()

# Part (b)
# Amplitude highest at pi/2 and -pi/2 at the change in sign/discontinuity in square wave

# The fourier graph appears to squeeze at pi/2 and -pi/2 with increasing values of n
# Increasing the value of nmax -> inf would lead to a tendency to have a spike at -pi/2 and pi/2 for
# the fourier series graph as well!

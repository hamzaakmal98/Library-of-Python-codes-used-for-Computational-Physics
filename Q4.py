import numpy as np
import matplotlib.pyplot as plt

xmin, xmax, step = -10, 10, 1 / 1000
x = np.arange(xmin, xmax, step)

mu = 0
sigma = 0.5
amp = 1 / (sigma * np.sqrt(2 * np.pi))
gaussian = amp * np.exp(-0.5 * ((x - mu) / sigma) ** 2)

sigma = 1
amp = 1 / (sigma * np.sqrt(2 * np.pi))
gaussian1 = amp * np.exp(-0.5 * ((x - mu) / sigma) ** 2)

sigma = 1.5
amp = 1 / (sigma * np.sqrt(2 * np.pi))
gaussian2 = amp * np.exp(-0.5 * ((x - mu) / sigma) ** 2)

plt.figure(figsize=(8, 5))
plt.plot(x, gaussian)
plt.plot(x, gaussian1)
plt.plot(x, gaussian2)
# plt.plot(x,f_prime)

plt.xlabel("x")
plt.ylabel("g(x)")
plt.title("Normalized Gaussian Function")
plt.grid()
plt.show()


def integral(f, a, b, n):
    h = (b - a) / n
    step = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        step += f(a + i * h)
    return h * step


def f(x):
    return amp * np.exp(-0.5 * ((x - mu) / sigma) ** 2)


a = -1000
b = 1000
n = 1000
result = integral(f, a, b, n)
print("They are normalized since the integrand from -inf to +inf is approaching 1 as shown: ")
print(result)


######################################################################################
#ALGORITHM FOR DERIVATIVE IS WRITTEN BELOW BUT ITS NOT PLOTTING SO I COMMENTED IT OUT
######################################################################################

# def central_difference_1(f, o, h):
#
#     return (f(o+h) - f(o-h)) / (2*h)
# o = 1
# h = 0.001
# f_prime = central_difference_1(exp,-0.5 * ((o - mu) / sigma)**2, h)

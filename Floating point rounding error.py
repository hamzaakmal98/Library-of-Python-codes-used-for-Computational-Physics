from math import sqrt


def f(x, nmax=100):
    for i in range(nmax):
        x = sqrt(x)

    for i in range(nmax):
        x = x ** 2
    return x

for xin in (5.0, 0.5):
    xout = f(xin)
    print(xin, xout)

#we get floating point rounding errors since the value is not a perfect square
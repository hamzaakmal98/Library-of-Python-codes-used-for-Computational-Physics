import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.exp(np.sin(2*x))

def df(x):
    hopt = np.sqrt(2*np.finfo(float).eps/np.abs(d2f(x)))
    hs = np.logspace(-1,-10,10,endpoint=True)
    errors = []
    for h in hs:
        approx = (f(x+h) - f(x))/h
        exact = df_exact(x)
        error = np.abs(approx - exact)
        errors.append(error)
    return hs, errors

def d2f(x):
    return -4*np.exp(np.sin(2*x))*np.sin(x)**2 + 2*np.exp(np.sin(2*x))*np.cos(2*x)

def df_exact(x):
    return 2*np.exp(np.sin(2*x))*np.cos(2*x)

hs, errors = df(0.5)

print('Step size\tAbsolute error')
for i in range(len(hs)):
    print('{:.1e}\t\t{:.1e}'.format(hs[i], errors[i]))

plt.loglog(hs, errors, '-o')
plt.xlabel('Step size')
plt.ylabel('Absolute error')
plt.title('Numerical approximation of df/dx')
plt.show()




















#
# Error analysis is an important tool for understanding the accuracy of numerical methods. In the context of approximating a function, such as taking its derivative, there are two types of errors to consider: approximation error and roundoff error.
#
# Approximation error arises from the fact that numerical methods can only approximate the exact solution. In the case of numerical differentiation, this means that the numerical approximation to the derivative may not be exactly equal to the true derivative. Approximation error can be reduced by using a smaller step size h.
#
# Roundoff error, on the other hand, is caused by the limited precision of numerical computations. When performing calculations on a computer, there are a limited number of digits that can be used to represent numbers. As a result, small errors can accumulate over the course of a calculation, leading to roundoff error. Roundoff error can be reduced by using higher-precision arithmetic, such as using double-precision instead of single-precision floating-point arithmetic.
#
# To derive expressions for the optimal step size hopt and the optimal error Eopt, we can use Taylor's theorem to approximate the error of the numerical differentiation method. For simplicity, we will consider the forward difference method for approximating the derivative of a function f(x).
#
# Using Taylor's theorem, we can write:
#
# f(x+h) = f(x) + hf'(x) + h^2/2 f''(x) + O(h^3)
#
# where O(h^3) denotes terms that are of order h^3 or higher. Rearranging this equation, we get:
#
# f'(x) = (f(x+h) - f(x))/h - h/2 f''(x) + O(h^2)
#
# This equation gives the exact value of the derivative, with an error term of order O(h^2). To derive the error of the numerical approximation, we replace f'(x) with its numerical approximation, which is given by:
#
# f'(x) ≈ (f(x+h) - f(x))/h
#
# Substituting this approximation into the error equation, we get:
#
# error = f'(x) - (f(x+h) - f(x))/h = -h/2 f''(x) + O(h^2)
#
# This equation tells us that the error of the numerical approximation is proportional to h and inversely proportional to the second derivative of the function f. Therefore, the optimal step size hopt can be found by minimizing the error equation with respect to h. This gives:
#
# hopt = sqrt(2 * epsilon / |f''(x)|)
#
# where epsilon is the machine epsilon, which is a measure of the precision of floating-point arithmetic. Note that this expression assumes that f''(x) is non-zero.
#
# The optimal error Eopt can be found by substituting hopt into the error equation:
#
# Eopt = |hopt/2 f''(x)| = sqrt(epsilon/2) |f''(x)|
#
# To produce numerical estimates for hopt and Eopt, we need to know the value of f''(x) at the point x. Depending on the function being differentiated, this may be difficult or impossible to determine analytically. In practice, we can use finite difference approximations to estimate the value of f''(x) numerically.
#
# Comparing these results to those for the first derivative, we can see that the optimal step size for numerical differentiation is proportional to the square root of the machine epsilon, while the optimal step size for numerical integration is proportional to the cube root of the machine epsilon. This means that numerical differentiation is generally more sensitive to roundoff error than numerical integration. However, the optimal error for numerical differentiation is also smaller than that for numerical integration, since the error is proportional to h^2 instead of h.


def central_difference_2(f, x, h):
    """
    Computes the second derivative of a function f at x using the central difference method
    with a step size of h.
    """
    return (f(x-h) - 2*f(x) + f(x+h)) / (h**2)

def central_difference_1(f, x, h):
    """
    Computes the first derivative of a function f at x using the central difference method
    with a step size of h.
    """
    return (f(x+h) - f(x-h)) / (2*h)

# Test case 1: calculate the first and second derivative of f(x) = x^2 at x=2 with h=0.1
def f(x):
    return x**2

x = 2
h = 0.1
f_prime = central_difference_1(f, x, h)
f_double_prime = central_difference_2(f, x, h)

print(f"Test case 1: x={x}, h={h}")
print(f"f'(x) = {f_prime:.2f}")
print(f"f''(x) = {f_double_prime:.2f}")
print()

# Test case 2: calculate the first and second derivative of f(x) = sin(x) at x=0 with h=0.01
from math import sin

x = 0
h = 0.01
f_prime = central_difference_1(sin, x, h)
f_double_prime = central_difference_2(sin, x, h)

print(f"Test case 2: x={x}, h={h}")
print(f"f'(x) = {f_prime:.2f}")
print(f"f''(x) = {f_double_prime:.2f}")
print()

# Test case 3: calculate the first and second derivative of f(x) = e^x at x=1 with h=0.001
from math import exp

x = 1
h = 0.001
f_prime = central_difference_1(exp, x, h)
f_double_prime = central_difference_2(exp, x, h)

print(f"Test case 3: x={x}, h={h}")
print(f"f'(x) = {f_prime:.2f}")
print(f"f''(x) = {f_double_prime:.2f}")
print()

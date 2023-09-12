import math
import matplotlib as plt
import numpy as np


# Justify Newtons method of finding roots: It is based on the idea of approximating the roots of a function by a
# linear approximation and then iteratively refining the estimate by using the slope of the function at the estimate.
# The method works well for smooth and well-behaved functions, and can converge quickly to the desired root. However,
# the method can be sensitive to the initial guess, and may fail to converge or converge to a different root if the
# function is not well-behaved. So we should be very careful that we dont use sus values as our guesses and ensure
# that we make an educated guess after some initial gruntwork on our own.


def f(x):
    return math.exp(x - math.sqrt(x)) - x


def df(x):
    return math.exp(x - math.sqrt(x)) * (1 - 0.5 / math.sqrt(x)) - 1


def newton_method(x_0, tolerance=1e-6, max_iterations=100):
    for i in range(max_iterations):
        f_value = f(x_0)
        df_value = df(x_0)
        x_0 -= f_value / df_value
        if abs(f_value) < tolerance:
            return x_0


root_1 = newton_method(0.5)
root_2 = newton_method(3)

print(root_1)
print(root_2)

# Graphing algorithm not working properly. Says only size-1 arrays can be converted to Python scalars.
# Same error as in Q4
# x_vals = np.linspace(0.5, 10, 50)
# y_vals = f(x_vals)
# plt.plot(x_vals, y_vals)
# plt.axhline(y=0, color='k', lw=0.5)
# plt.axvline(x=root_1, color='r', linestyle='--', lw=0.5)
# plt.axvline(x=root_2, color='r', linestyle='--', lw=0.5)
# plt.xlabel('x')
# plt.ylabel('f(x)')
# plt.title('Graph of f(x) = exp(x-math.sqrt(x)) - x')
# plt.show()

import numpy as np

def numerical_derivative(f, x, h=0.0001):
    """
    Computes the numerical derivative of a function f at point x using the
    finite difference method.
    """
    return (f(x + h) - f(x - h)) / (2 * h)

# Example usage
f = lambda x: x**2  # Define a function
x = 3.0  # Point at which to evaluate the derivative
df_dx = numerical_derivative(f, x)  # Approximate the derivative
print(df_dx)  # Print the result

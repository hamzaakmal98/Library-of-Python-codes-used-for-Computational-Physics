def trapezoidal_rule(f, a, b, n):
    """Approximate the definite integral of f(x) from a to b by the trapezoidal rule.

    Args:
        f (function): Function to integrate.
        a (float): Lower limit of integration.
        b (float): Upper limit of integration.
        n (int): Number of trapezoids to use in the approximation.

    Returns:
        float: Approximation of the definite integral of f(x) from a to b.
    """
    h = (b - a) / n
    s = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        s += f(a + i*h)
    return h * s

def f(x):
    return x**2

a = 0
b = 1
n = 100

approx = trapezoidal_rule(f, a, b, n)
print(approx)

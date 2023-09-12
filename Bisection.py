def bisection_method(f, a, b, tolerance):
    """Find root of function f given interval [a, b] and tolerance"""
    if f(a) * f(b) > 0:
        raise ValueError("f(a) and f(b) must have opposite signs")
    c = a
    while (b-a)/2 > tolerance:
        c = (a+b)/2
        if f(c) == 0:
            return c
        elif f(c)*f(a) < 0:
            b = c
        else:
            a = c
    return c

# Example usage
f = lambda x: x**2 - 4
root = bisection_method(f, 0, 2, 0.0001)
print(root)

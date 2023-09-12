def riemann_sum(f, a, b, n):
    """Approximate the definite integral of f from a to b using n subintervals."""
    dx = (b - a) / n  # width of each subinterval
    x = a + dx / 2    # midpoint of the first subinterval
    sum = 0
    for i in range(n):
        sum += f(x) * dx
        x += dx
    return sum

def f(x):
    return 1 / (1 + x ** 3)

a = 0
b = 10
n = 1000000  # using a large number of subintervals for better accuracy

integral = riemann_sum(f, a, b, n)
print(f"The definite integral of f(x) = 1/(1+x**3) from {a} to {b} is approximately {integral:.6f}")

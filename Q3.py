def integral(f, a, b, n):
    h = (b - a) / n
    step = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        step += f(a + i * h)
    return h * step


def f(x):
    return x ** 2


a = 0
b = 10
n = 1000

result = integral(f, a, b, n)
print(result)
# n = 50 gives 333.40000000000015
# n = 10 gives 335.0
# n = 2 gives 375.0
# n = 1000 gives 333.33350000000013

# The exact answer is 10**3/3. We see that as we increase the number of intervals 'n'
# we start getting closer and closer to the correct result.

def tetration(x, n):
    """
    Computes x raised to the power of itself n times using recursive tetration.
    """
    if n == 1:
        return x
    else:
        return x ** tetration(x, n-1)

x = 5
n = 3
result = tetration(x, n)
num_digits = len(str(result))
print(f"{x}^{n} has {num_digits} digits")

x = 2
n = 5
result = tetration(x, n)
num_digits = len(str(result))
print(f"{x}^{n} has {num_digits} digits")

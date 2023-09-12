def factorial_iterative(n):
    """
    Computes the factorial of a non-negative integer n iteratively.
    """
    if n < 0:
        raise ValueError("n must be non-negative")

    result = 1
    for i in range(2, n+1):
        result *= i
    print(f"{n}! = {result}")
    return result

# Example usage:
factorial_iterative(5)

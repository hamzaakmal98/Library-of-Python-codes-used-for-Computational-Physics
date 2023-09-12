def hailstone(n):
    """
    Generates the hailstone sequence starting at n.
    """
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence

def hailstone_stopping_time(n):
    """
    Generates the hailstone sequence starting at n and returns its stopping time.
    """
    stopping_time = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        stopping_time += 1
    return stopping_time

# Test the Collatz conjecture for the hailstone sequences starting with 1 ≤ n ≤ 100
for n in range(1, 101):
    stopping_time = hailstone_stopping_time(n)
    print(f"The stopping time of the hailstone sequence starting at {n} is {stopping_time}")

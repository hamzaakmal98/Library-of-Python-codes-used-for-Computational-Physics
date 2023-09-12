def sieve_of_eratosthenes(n):
    """
    Generates all prime numbers up to n using the Sieve of Eratosthenes algorithm.
    """
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False

    for i, is_prime in enumerate(sieve):
        if is_prime:
            yield i
            for j in range(i * i, n + 1, i):
                sieve[j] = False

# Use the sieve to find all primes under 10000
primes = list(sieve_of_eratosthenes(10000))

# Print the primes
for i, prime in enumerate(primes):
    print(f"{i + 1}: {prime}")

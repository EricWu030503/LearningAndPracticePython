def sieve_of_eratosthenes(n):
    # Create a boolean array "is_prime[0..n]" and initialize all entries as True
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not primes

    p = 2
    while p * p <= n:
        if is_prime[p]:
            # Mark all multiples of p as not prime
            for multiple in range(p * p, n + 1, p):
                is_prime[multiple] = False
        p += 1

    # Return list of prime numbers
    return [i for i, prime in enumerate(is_prime) if prime]

# Example usage
n = 50
primes = sieve_of_eratosthenes(n)
print(f"Prime numbers up to {n}:", primes)

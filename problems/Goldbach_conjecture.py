def sieve_of_eratosthenes(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not primes

    p = 2
    while p * p <= limit:
        if is_prime[p]:
            for multiple in range(p * p, limit + 1, p):
                is_prime[multiple] = False
        p += 1
    return is_prime

is_prime = sieve_of_eratosthenes(1000000)


n = int(input())
while n != 0:
    b = n - 3
    a = 3
    while (not is_prime[b] or not is_prime[a]) and b > a:
        b -= 2
        a +=2
    if not is_prime[b] or not is_prime[a]:
        print("Goldbach's conjecture is wrong.")
    else:
        print(f"{n} = {a} + {b}")

    n = int(input())
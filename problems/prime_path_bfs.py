"""
This program finds the shortest path between two 4-digit prime numbers,
where each step in the path changes exactly one digit and results in another valid 4-digit prime.
It uses Breadth-First Search (BFS) to explore the space of valid primes efficiently.

Problem Summary:
- Given multiple test cases, each with a pair of 4-digit prime numbers (start and end),
  determine the minimum number of single-digit transformations required to turn the start into the end.
- All intermediate numbers must also be 4-digit primes.
- If no such path exists, report that it's impossible.

Approach:
- Generate all 4-digit primes using the Sieve of Eratosthenes.
- Build neighbors by changing one digit at a time and validating primality.
- Use BFS for shortest path discovery in an unweighted graph.
"""

from collections import deque

# Generate all 4-digit prime numbers using Sieve of Eratosthenes
def generate_four_digit_primes():
    is_prime = [True] * 10000
    is_prime[0:2] = [False, False]
    for i in range(2, 100):
        if is_prime[i]:
            for j in range(i*i, 10000, i):
                is_prime[j] = False
    return {i for i in range(1000, 10000) if is_prime[i]}

# Generate all valid neighbors (1-digit change that is also a 4-digit prime)
def get_neighbors(num, primes):
    neighbors = []
    num_str = str(num)
    for i in range(4):
        for d in '0123456789':
            if i == 0 and d == '0':  # no leading zero
                continue
            if num_str[i] != d:
                new_num = int(num_str[:i] + d + num_str[i+1:])
                if new_num in primes:
                    neighbors.append(new_num)
    return neighbors

# BFS to find the minimum number of steps from start to end
def bfs(start, end, primes):
    visited = set()
    queue = deque([(start, 0)])
    visited.add(start)
    while queue:
        current, steps = queue.popleft()
        if current == end:
            return steps
        for neighbor in get_neighbors(current, primes):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, steps + 1))
    return -1  # Impossible

# Main solver
def solve():
    T = int(input())
    primes = generate_four_digit_primes()
    for _ in range(T):
        start, end = map(int, input().split())
        steps = bfs(start, end, primes)
        print(steps if steps != -1 else "Impossible")

# Run
if __name__ == "__main__":
    solve()


# 🐜 Problem: Ants on a Pole
# -------------------------------------
# An army of ants walk on a horizontal pole of length `l` cm.
# Each ant walks at a constant speed of 1 cm/s.
# When an ant reaches an end of the pole, it falls off.
# When two ants meet, they turn around and walk in opposite directions.
#
# You are given the positions of all ants, but **not their initial directions**.
# Your task is to compute:
#   1. The **earliest possible time** when all ants could fall off.
#   2. The **latest possible time** it might take for all ants to fall off.
#
# 🧠 Key Insight:
# - Ant collisions are equivalent to "identity swaps", so we can model each ant as moving straight.
# - The best-case (earliest) time = max of min(x, l - x) over all ants
# - The worst-case (latest) time = max of max(x, l - x) over all ants

# 📥 Input:
# - The first line contains an integer T: the number of test cases.
# - For each test case:
#     - A line with two integers: l (pole length) and n (number of ants)
#     - Then n lines follow, each with a single integer x_i (position of the i-th ant)
#
# 📤 Output:
# - For each test case, print two integers separated by space:
#     - The earliest possible time
#     - The latest possible time
# -------------------------------------

num_cases = int(input())
for _ in range(num_cases):
    l, n = map(int, input().split())
    min_time = 0
    max_time = 0
    for _ in range(n):
        x = int(input())
        # Best case: ant moves to nearest end
        min_time = max(min_time, min(x, l - x))
        # Worst case: ant moves to farthest end
        max_time = max(max_time, max(x, l - x))
    print(min_time, max_time)

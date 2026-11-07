# apple_partition.py

# =======================
# Problem Description:
# =======================
# This program computes the number of distinct ways to place `m` identical apples
# into `n` identical plates, where each plate can hold zero or more apples.
#
# Two arrangements are considered the same if the number of apples in each plate
# is the same, regardless of the order of the plates.
#
# Example:
# m = 7 apples, n = 3 plates
# Valid partitions (unordered):
# (7,0,0), (6,1,0), (5,2,0), (5,1,1), (4,3,0), (4,2,1), (3,3,1), (3,2,2)
# Total = 8

def count_partitions(m, n, memo=None):
    """
    Count the number of ways to distribute `m` identical apples
    into `n` identical plates using recursive construction.

    Arguments:
    - m: number of apples
    - n: number of plates
    - memo: a dictionary for memoization to speed up recursion

    Returns:
    - Integer: number of valid partitions
    """
    if memo is None:
        memo = {}

    # Check if the result is already computed
    if (m, n) in memo:
        return memo[(m, n)]

    # Base Case 1: Only one plate — all apples must go there
    if n == 1 or m == 0:
        return 1

    # Base Case 2: More plates than apples — extra plates must be empty,
    # so it reduces to m apples and m plates
    if n > m:
        result = count_partitions(m, m, memo)
    else:
        # Recursive Case:
        # Option 1: At least one plate is empty → count_partitions(m, n - 1)
        # Option 2: Each plate gets at least 1 apple → remove 1 from each plate
        #           and distribute remaining m - n apples across n plates
        result = count_partitions(m, n - 1, memo) + count_partitions(m - n, n, memo)

    # Save result for memoization
    memo[(m, n)] = result
    return result

# ================
# Example Usage
# ================
if __name__ == "__main__":
    m = 7  # number of apples
    n = 3  # number of plates
    print("Number of distinct distributions:", count_partitions(m, n))  # Output: 8

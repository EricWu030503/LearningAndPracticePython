# Problem: Fractional Knapsack
# ---------------------------------------------
# You are given two lists:
#   - values[i]: the value of the i-th item
#   - weights[i]: the weight of the i-th item
# and a maximum weight capacity W for the knapsack.
#
# You can take any fraction of an item.
# The goal is to maximize the total value in the knapsack.
#
# Strategy:
#   - Take items in decreasing order of value-to-weight ratio.
#   - If you can't take the full item, take as much as possible (i.e., a fraction).
#   - Stop when the knapsack is full.

def fractional_knapsack(values, weights, W):
    n = len(values)
    # Create a list of tuples: (value, weight, value/weight ratio)
    items = sorted(
        [(values[i], weights[i], values[i] / weights[i]) for i in range(n)],
        key=lambda x: x[2],
        reverse=True
    )

    total_value = 0.0
    for value, weight, ratio in items:
        if W == 0:
            break
        take_weight = min(W, weight)
        total_value += take_weight * ratio
        W -= take_weight

    return total_value

# Problem: Interval Scheduling (Activity Selection Problem)
#
# You are given `n` activities with start and end times.
# Select the maximum number of non-overlapping activities that can be performed by a single person.
# Each activity i has a start time `start[i]` and end time `end[i]`.
# You can only attend non-overlapping activities.
#
# Strategy: Greedy algorithm — always select the next activity that finishes the earliest.
# This ensures the largest number of total activities can be accommodated.

def max_activities(start, end):
    activities = sorted(zip(start, end), key=lambda x: x[1])  # sort by end time
    count = 0
    last_end_time = 0
    selected = []

    for s, e in activities:
        if s >= last_end_time:
            count += 1
            last_end_time = e
            selected.append((s, e))

    return count, selected

# Example usage:
start_times = [1, 3, 0, 5, 8, 5]
end_times   = [2, 4, 6, 7, 9, 9]

count, chosen = max_activities(start_times, end_times)
print("Max number of activities:", count)
print("Selected intervals:", chosen)

# Suppose we have two options for the next activity, a and b,
# both starting after the previous selected activity ends.
# If activity a ends earlier than activity b, then choosing a
# leaves more room for scheduling additional future activities.
# Therefore, choosing the activity with the earliest end time
# maximizes the potential number of non-overlapping activities
# and is never worse than choosing one that ends later.
# This is why the greedy strategy of picking the earliest ending
# activity gives the optimal solution.

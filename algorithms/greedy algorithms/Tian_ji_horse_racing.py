# ---------------------------------------------
# 🐎 Problem: Tian Ji's Horse Racing Strategy
#
# In ancient China, General Tian Ji races his horses against the King's.
# Each player has n horses, each with a speed.
# Each round, both choose one horse to race. The faster horse wins +200 silver dollars.
# If Tian Ji loses a round, he loses -200 silver dollars. A tie gives 0.
# The goal is to maximize the total winnings by smartly matching horses.
#
# 🎯 Strategy:
# This is a greedy matching problem, similar to a bipartite matching graph.
# You must choose the optimal pairing to maximize Tian Ji's score.
#
# 🧾 Input:
# - Multiple test cases (up to 50)
# - Each test case starts with an integer n (1 ≤ n ≤ 1000)
# - Next line: n integers = Tian Ji's horse speeds
# - Next line: n integers = King's horse speeds
# - Ends with a line containing 0
#
# 🧾 Output:
# - For each test case, output a single line with the maximum silver dollars Tian Ji can earn
# ---------------------------------------------

def tian_ji_race():
    while True:
        n = int(input())
        if n == 0:
            break

        tian_horses = list(map(int, input().split()))
        king_horses = list(map(int, input().split()))

        # 🧠 Greedy Strategy:
        # Sort both lists in descending order — we want to match best vs best if possible
        tian_horses.sort(reverse=True)
        king_horses.sort(reverse=True)

        t_left, t_right = 0, n - 1
        k_left, k_right = 0, n - 1
        score = 0

        while t_left <= t_right:
            # ✅ Case 1: Tian's fastest can beat King's fastest → Win
            if tian_horses[t_left] > king_horses[k_left]:
                score += 200
                t_left += 1
                k_left += 1

            # ✅ Case 2: Tian's slowest can beat King's slowest → Win
            elif tian_horses[t_right] > king_horses[k_right]:
                score += 200
                t_right -= 1
                k_right -= 1

            # ❌ Case 3: Cannot win → Sacrifice slowest against King's strongest
            else:
                if tian_horses[t_right] < king_horses[k_left]:
                    score -= 200
                t_right -= 1
                k_left += 1

        print(score)

# Run the function
tian_ji_race()

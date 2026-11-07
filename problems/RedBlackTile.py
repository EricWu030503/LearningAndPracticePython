# Problem Description:
# ---------------------
# You are given a 2D grid representing a rectangular room with tiles.
# Each tile is either:
# - '.' : a black tile the man can walk on
# - '#' : a wall tile the man cannot pass
#
# There is exactly one starting tile marked with '@', representing the man's starting position.
#
# From any black tile ('.' or '@'), the man can move up, down, left, or right to another black tile.
# The goal is to calculate how many tiles the man can reach, including the starting tile.

# Input:
# -------
# The input consists of multiple test cases. Each test case begins with two integers:
#   w h
# where:
#   w = width of the room (number of columns)
#   h = height of the room (number of rows)
#   (1 <= w, h <= 20)
#
# Following are h lines each containing w characters representing the room map.
# Each character is either:
#   '#' (wall), '.' (black tile), or '@' (starting point)
#
# The input ends with a line containing two zeros: 0 0

# Output:
# --------
# For each test case, output a single line containing the number of tiles the man can reach.

import sys
sys.setrecursionlimit(10000)  # in case of large input

def dfs(x, y, grid, visited, H, W):
    if not (0 <= x < H and 0 <= y < W):
        return 0
    if grid[x][y] == '#' or visited[x][y]:
        return 0
    visited[x][y] = True
    count = 1
    for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
        count += dfs(x + dx, y + dy, grid, visited, H, W)
    return count

while True:
    line = sys.stdin.readline()
    if not line:
        break
    W, H = map(int, line.strip().split())
    if W == 0 and H == 0:
        break

    grid = []
    start_x = start_y = -1
    for i in range(H):
        row = sys.stdin.readline().strip()
        grid.append(row)
        if '@' in row:
            start_x, start_y = i, row.index('@')

    visited = [[False]*W for _ in range(H)]
    result = dfs(start_x, start_y, grid, visited, H, W)
    print(result)

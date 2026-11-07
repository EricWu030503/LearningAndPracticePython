# reachability.py

"""
This file demonstrates three approaches to solving reachability problems in graphs:
1. DFS: Depth-First Search (on-demand reachability)
2. BFS: Breadth-First Search (on-demand reachability, shortest path if unweighted)
3. Warshall’s Algorithm: Precomputes reachability between all pairs of nodes
"""

from collections import deque

# ----------------------------
# PART 1: Using DFS
# ----------------------------
def dfs(graph, start, target, visited=None):
    """
    DFS for reachability in both directed and undirected graphs.
    Returns True if there's a path from start to target.
    """
    if visited is None:
        visited = set()
    if start == target:
        return True
    visited.add(start)
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            if dfs(graph, neighbor, target, visited):
                return True
    return False

# ----------------------------
# PART 2: Using BFS
# ----------------------------
def bfs(graph, start, target):
    """
    BFS for reachability in both directed and undirected graphs.
    Returns True if there's a path from start to target.
    Also useful when shortest path (in unweighted graphs) is needed.
    """
    visited = set()
    queue = deque([start])
    visited.add(start)
    while queue:
        node = queue.popleft()
        if node == target:
            return True
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return False

# ----------------------------
# PART 3: Warshall's Algorithm
# ----------------------------
def warshall(adj_matrix):
    """
    Warshall's Algorithm for computing transitive closure (reachability)
    Input: adjacency matrix (n x n) where adj[i][j] = 1 if i → j
    Output: modified matrix with reachability info: reachable[i][j] = 1 if path exists
    """
    n = len(adj_matrix)
    reach = [row[:] for row in adj_matrix]  # Deep copy
    # intermediate nodes must be in the outermost loop so that we don't skip any intermediate path
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if reach[i][k] and reach[k][j]:
                    reach[i][j] = 1
    return reach

# ----------------------------
# Example usage
# ----------------------------
if __name__ == "__main__":
    # Undirected graph represented as adjacency list
    undirected_graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D'],
        'C': ['A', 'E'],
        'D': ['B'],
        'E': ['C'],
    }

    # Directed graph represented as adjacency list
    directed_graph = {
        'A': ['B'],
        'B': ['C'],
        'C': ['D'],
        'D': [],
    }

    print("DFS (Undirected): A to D:", dfs(undirected_graph, 'A', 'D'))
    print("BFS (Undirected): A to E:", bfs(undirected_graph, 'A', 'E'))

    print("DFS (Directed): A to D:", dfs(directed_graph, 'A', 'D'))
    print("BFS (Directed): A to E:", bfs(directed_graph, 'A', 'E'))

    # Warshall example (directed graph as adjacency matrix)
    adj_matrix = [
        [0, 1, 0, 0],  # A → B
        [0, 0, 1, 0],  # B → C
        [0, 0, 0, 1],  # C → D
        [0, 0, 0, 0]   # D
    ]
    print("Warshall Reachability Matrix:")
    reachable = warshall(adj_matrix)
    for row in reachable:
        print(row)

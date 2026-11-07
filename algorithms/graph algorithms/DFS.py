# Depth-First Search using Recursion and Stack (Iterative)

# Sample graph as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# -----------------------------------
# DFS using recursion
# -----------------------------------
def dfs_recursive(graph, node, visited=None):
    if visited is None:
        visited = set()
    print("Visited (rec):", node)
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)

# -----------------------------------
# DFS using an explicit stack (iterative)
# -----------------------------------
def dfs_iterative(graph, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            print("Visited (iter):", node)
            visited.add(node)
            # Push neighbors in reverse order to simulate recursion order
            stack.extend(reversed(graph[node]))

# -----------------------------------
# Main function to run both methods
# -----------------------------------
def main():
    print("Recursive DFS starting from A:")
    dfs_recursive(graph, 'A')

    print("\nIterative DFS starting from A:")
    dfs_iterative(graph, 'A')

if __name__ == "__main__":
    main()

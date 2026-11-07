# ----------------------------------------------------------
# Case 1 & 2: Shortest Path in Unweighted Graph (Directed/Undirected)
# Algorithm: Breadth-First Search (BFS)
# ----------------------------------------------------------

from collections import deque

def bfs_shortest_path(graph, source, target):
    """
    Finds the shortest path and its length in an unweighted graph using BFS.

    :param graph: dict, adjacency list representation (directed or undirected).
    :param source: starting node
    :param target: target node
    :return: tuple (distance, path) if path exists, else (-1, [])
    """
    queue = deque([(source, [source])]) # store the unprocessed node and path to that node
    visited = set([source])

    while queue:
        current, path = queue.popleft()
        if current == target:
            return len(path) - 1, path  # path length is number of edges = nodes - 1
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor])) # note that we only extend the path based on the path to the current node

    return -1, []  # unreachable

# Example usage:
if __name__ == "__main__":
    # Undirected, Unweighted Graph
    graph_undirected = {
        0: [1, 2],
        1: [0, 3],
        2: [0, 3],
        3: [1, 2, 4],
        4: [3]
    }

    # Directed, Unweighted Graph
    graph_directed = {
        0: [1, 2],
        1: [3],
        2: [3],
        3: [4],
        4: []
    }

    print("Undirected Graph Shortest Path from 0 to 4:")
    dist, path = bfs_shortest_path(graph_undirected, 0, 4)
    print(f"Distance: {dist}, Path: {path}")

    print("\nDirected Graph Shortest Path from 0 to 4:")
    dist, path = bfs_shortest_path(graph_directed, 0, 4)
    print(f"Distance: {dist}, Path: {path}")

# ----------------------------------------------------------
# Case 3 & 4: Shortest Path in Weighted Graph (Directed/Undirected)
# Algorithm: Dijkstra’s Algorithm (non-negative weights only)
# ----------------------------------------------------------

import heapq

def dijkstra_shortest_path(graph, source, target): # Distance-First Search
    """
    Finds the shortest path and its distance in a weighted graph using Dijkstra's algorithm.

    :param graph: dict, adjacency list representation where graph[u] = list of (v, weight)
    :param source: starting node
    :param target: target node
    :return: tuple (distance, path) if path exists, else (float('inf'), [])
    """
    dist = {node: float('inf') for node in graph} # Stores the shortest known distance from the source node to every other node
    prev = {node: None for node in graph} # stores the previous node in its shortest path from source （note that the shortest path to the previous node must be included in the shortest path to this node)
    dist[source] = 0
    heap = [(0, source)] # stores the distance from the source and the node sorted by distance(min first)

    while heap:
        current_dist, u = heapq.heappop(heap) # process the node with shortest distance

        if u == target:
            break

        if current_dist > dist[u]:
            continue

        for v, weight in graph[u]:
            new_dist = current_dist + weight
            if new_dist < dist[v]:
                dist[v] = new_dist
                prev[v] = u
                heapq.heappush(heap, (new_dist, v))

    # Reconstruct path
    if dist[target] == float('inf'):
        return float('inf'), []

    path = []
    curr = target
    while curr is not None:
        path.append(curr)
        curr = prev[curr]
    path.reverse()
    return dist[target], path

# Example usage:
if __name__ == "__main__":
    # Weighted Undirected Graph
    graph_undirected = {
        0: [(1, 2), (2, 4)],
        1: [(0, 2), (3, 1)],
        2: [(0, 4), (3, 3)],
        3: [(1, 1), (2, 3), (4, 5)],
        4: [(3, 5)]
    }

    # Weighted Directed Graph
    graph_directed = {
        0: [(1, 2), (2, 4)],
        1: [(3, 1)],
        2: [(3, 3)],
        3: [(4, 5)],
        4: []
    }

    print("Undirected Weighted Graph Shortest Path from 0 to 4:")
    dist, path = dijkstra_shortest_path(graph_undirected, 0, 4)
    print(f"Distance: {dist}, Path: {path}")

    print("\nDirected Weighted Graph Shortest Path from 0 to 4:")
    dist, path = dijkstra_shortest_path(graph_directed, 0, 4)
    print(f"Distance: {dist}, Path: {path}")

# ----------------------------------------------------------
# Case 5: All-Pairs Shortest Path directed/undirected, weighted and unweighted(weight = 1 for every edge) graph (Negative Weights Allowed)
# Algorithm: Floyd-Warshall Algorithm
# ----------------------------------------------------------

def floyd_warshall(graph):
    """
    Computes shortest distances and paths between all pairs using Floyd-Warshall algorithm.

    :param graph: dict of dicts, e.g. graph[u][v] = weight
    :return: distance matrix and predecessor matrix
    """
    nodes = list(graph.keys())
    n = len(nodes)
    dist = {u: {v: float('inf') for v in nodes} for u in nodes}
    pred = {u: {v: None for v in nodes} for u in nodes}

    # Initialize distances and predecessors
    for u in nodes:
        dist[u][u] = 0
        for v in graph[u]:
            dist[u][v] = graph[u][v]
            pred[u][v] = u

    # Main algorithm
    for k in nodes:
        for i in nodes:
            for j in nodes:
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    pred[i][j] = pred[k][j]

    return dist, pred

def reconstruct_fw_path(start, end, pred):
    """
    Reconstructs shortest path from Floyd-Warshall result.

    :param start: start node
    :param end: end node
    :param pred: predecessor matrix from floyd_warshall
    :return: list of nodes forming the path
    """
    if pred[start][end] is None:
        return []

    path = [end]
    while end != start:
        end = pred[start][end]
        path.append(end)
    path.reverse()
    return path

# Example usage
if __name__ == "__main__":
    # Directed graph with negative weights but no negative cycles
    graph = {
        0: {1: 3, 2: 8, 4: -4},
        1: {3: 1, 4: 7},
        2: {1: 4},
        3: {0: 2, 2: -5},
        4: {3: 6}
    }

    dist, pred = floyd_warshall(graph)

    print("Floyd-Warshall Shortest Distance from 0 to 2:")
    print("Distance:", dist[0][2])
    print("Path:", reconstruct_fw_path(0, 2, pred))

    print("\nFloyd-Warshall Shortest Distance from 1 to 2:")
    print("Distance:", dist[1][2])
    print("Path:", reconstruct_fw_path(1, 2, pred))

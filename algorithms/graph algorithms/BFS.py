from collections import deque

def bfs(graph, start_vertex):
    queue = deque()  # Queue to keep track of vertices to visit
    visited = set()  # Set to keep track of visited vertices

    # Mark the start vertex as visited and enqueue it
    visited.add(start_vertex)
    queue.append(start_vertex)

    while queue:
        current_vertex = queue.popleft()  # Dequeue a vertex from the queue
        print("Visited:", current_vertex)  # Process the current vertex

        # Iterate through all adjacent vertices of the dequeued vertex
        for adjacent_vertex in graph.list_all_adjacent(current_vertex):
            if adjacent_vertex not in visited:
                visited.add(adjacent_vertex)      # Mark it as visited
                queue.append(adjacent_vertex)     # Enqueue it for further exploration

# Example usage
class AdjacencyMatrixGraph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.matrix = [[0] * num_vertices for _ in range(num_vertices)]

    def add_edge(self, u, v):
        self.matrix[u][v] = 1
        self.matrix[v][u] = 1  # Undirected graph

    def list_all_adjacent(self, vertex):
        return [i for i, val in enumerate(self.matrix[vertex]) if val == 1]

if __name__ == "__main__":
    graph = AdjacencyMatrixGraph(5)

    # Manually adding edges to the graph for demonstration
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 3)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)

    # Starting BFS from vertex 0
    bfs(graph, 0)

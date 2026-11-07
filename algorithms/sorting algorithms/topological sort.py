"""
Topological Sort (Kahn's Algorithm) - Comprehensive Overview

What is Topological Sort?
-------------------------
Topological sorting is a linear ordering of vertices in a Directed Acyclic Graph (DAG) such that
for every directed edge u → v, vertex u appears before v in the ordering.

When Can It Be Used?
--------------------
Topological sort can be used when:
- The graph is directed.
- The graph is acyclic (no cycles).

Typical Use Cases:
------------------
- Task scheduling (e.g., tasks with dependencies)
- Course prerequisite planning
- Build systems (e.g., compile files with dependencies)
- Dependency resolution in package managers

Kahn’s Algorithm (BFS-based):
-----------------------------
1. Calculate in-degree (number of incoming edges) for all vertices.
2. Enqueue all nodes with in-degree 0.
3. While queue is not empty:
    a. Pop a node, add to topological order.
    b. For each of its neighbors, reduce in-degree by 1.
    c. If in-degree becomes 0, add neighbor to queue.
4. If topological order includes all nodes, success. Otherwise, there's a cycle.
"""

from collections import defaultdict, deque

def topological_sort_kahn(graph):
    indegree = defaultdict(int)
    for u in graph:
        for v in graph[u]:
            indegree[v] += 1
        if u not in indegree:
            indegree[u] = 0  # Ensure all nodes are present

    queue = deque([node for node in graph if indegree[node] == 0])
    topo_order = []

    while queue:
        u = queue.popleft()
        topo_order.append(u)
        for v in graph[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                queue.append(v)

    if len(topo_order) != len(indegree):
        raise ValueError("Graph contains a cycle. Topological sort not possible.")

    return topo_order


# ---------------------------
# Example 1: Basic DAG example
# ---------------------------
print("Example 1: Basic DAG Topological Sort")

dag_example = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D'],
    'D': []
}

print("Graph:")
for node in dag_example:
    print(f"{node} → {dag_example[node]}")

topo_order = topological_sort_kahn(dag_example)
print("Topological Order:", topo_order)


# ------------------------------------------
# Example 2: Real-world - Course prerequisites
# ------------------------------------------
print("\nExample 2: Course Prerequisite Planning")

course_graph = {
    'Intro to Programming': ['Data Structures'],
    'Data Structures': ['Algorithms'],
    'Algorithms': ['Machine Learning'],
    'Machine Learning': [],
    'Computer Architecture': ['Operating Systems'],
    'Operating Systems': [],
    'Discrete Math': ['Algorithms'],
}

print("Course Dependency Graph:")
for course in course_graph:
    print(f"{course} → {course_graph[course]}")

course_order = topological_sort_kahn(course_graph)
print("Suggested Course Order:", course_order)

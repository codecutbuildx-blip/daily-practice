# Topological Sort in Python
=====================================

This code demonstrates a topological sort algorithm in Python. A topological sort is a linear ordering of vertices in a directed acyclic graph (DAG) such that for every directed edge u -> v, vertex u comes before v in the ordering.

```python
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for _ in range(vertices)]

    # Function to add an edge to the graph
    def add_edge(self, u, v):
        self.graph[u].append(v)

    # Function to perform topological sort using DFS
    def topological_sort_util(self, v, visited, stack):
        visited[v] = True
        for i in self.graph[v]:
            if visited[i] == False:
                self.topological_sort_util(i, visited, stack)
        stack.insert(0, v)

    # Function to perform topological sort
    def topological_sort(self):
        visited = [False] * (self.V)
        stack = []
        for i in range(self.V):
            if visited[i] == False:
                self.topological_sort_util(i, visited, stack)
        return stack


# Example usage
g = Graph(6)
g.add_edge(5, 2)
g.add_edge(5, 0)
g.add_edge(4, 0)
g.add_edge(4, 1)
g.add_edge(2, 3)
g.add_edge(3, 1)

print("Topological Sort:")
print(g.topological_sort())
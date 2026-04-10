# Topological Sort in Python

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        # Create a list to store the graph
        self.graph = [[] for _ in range(vertices)]

    # Function to add an edge to the graph
    def add_edge(self, u, v):
        self.graph[u].append(v)

    # Function to check if it is possible to find a topological sort of the given graph
    def has_topological_sort(self):
        # Create a list to store the in-degree of each vertex
        in_degree = [0] * self.V

        # Calculate the in-degree of each vertex
        for i in range(self.V):
            for j in self.graph[i]:
                in_degree[j] += 1

        # Create a queue and enqueue vertices with in-degree 0
        q = []
        for i in range(self.V):
            if in_degree[i] == 0:
                q.append(i)

        # Perform BFS
        while q:
            vertex = q.pop(0)
            print(vertex, end=" ")

            # Decrease the in-degree of adjacent vertices by 1
            for neighbor in self.graph[vertex]:
                in_degree[neighbor] -= 1

                # Enqueue if there are no more incoming edges
                if in_degree[neighbor] == 0:
                    q.append(neighbor)

        # If there are remaining vertices with non-zero in-degree, then graph has cycle and does not have topological sort
        for i in range(self.V):
            if in_degree[i] != 0:
                return False

        return True


# Test the code
g = Graph(6)
g.add_edge(5, 2)
g.add_edge(5, 0)
g.add_edge(4, 0)
g.add_edge(4, 1)
g.add_edge(2, 3)
g.add_edge(3, 1)

print("Topological Sort exists")
if g.has_topological_sort():
    print("Topological order is")
else:
    print("Graph has cycle and does not have topological sort")
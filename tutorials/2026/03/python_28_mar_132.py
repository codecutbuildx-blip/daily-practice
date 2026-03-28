# Topological Sort in Python

class Graph:
    def __init__(self, vertices):
        # Initialize the graph with a given number of vertices
        self.V = vertices
        self.graph = [[] for _ in range(vertices)]

    # Function to add an edge from vertex 'v' to vertex 'w'
    def add_edge(self, v, w):
        # Add an edge from v to w
        self.graph[v].append(w)

    # Function to check if a vertex can be included in the topological sort
    def is safe(self, v, visited, stack):
        # If graph[v] not empty, then return False
        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                return False

        # Return True if no such neighbors exist
        return True

    # Function to perform topological sort
    def topological_sort_util(self, v, visited, stack):
        # Mark vertex as visited
        visited[v] = True

        # Recur for all the vertices adjacent to v
        for i in self.graph[v]:
            if not visited[i]:
                if not self.is_safe(i, visited, stack):
                    return False

        # Push 'v' into the stack which is topological order
        stack.append(v)

        # Return True if we have successfully colored all vertices
        return True

    # Function to perform topological sort
    def topological_sort(self):
        # Create a set of visited vertices and a stack for storing the result
        visited = [False] * (self.V)
        stack = []

        # Call the recursive helper function
        for i in range(self.V):
            if not visited[i]:
                if not self.topological_sort_util(i, visited, stack):
                    return None

        # Return the topological order
        return stack[::-1]


# Example usage:
g = Graph(6)
g.add_edge(5, 2)
g.add_edge(5, 0)
g.add_edge(4, 0)
g.add_edge(4, 1)
g.add_edge(2, 3)
g.add_edge(3, 1)

print("Topological Sort:")
top_sort = g.topological_sort()
if top_sort:
    print(top_sort)
else:
    print("Graph has cycle")
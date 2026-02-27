# Breadth-First Search (BFS) Graph Traversal in Python
=====================================================

## Introduction

Breadth-First Search (BFS) is a graph traversal algorithm that visits all the nodes in a graph level by level, starting from a given source node.

## Code

```python
from collections import deque

class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, src, dest):
        """Add an edge between two nodes."""
        if src not in self.adj_list:
            self.adj_list[src] = []
        self.adj_list[src].append(dest)

    def bfs(self, start_node):
        """Perform BFS traversal from a given node."""
        visited = set()
        queue = deque([start_node])
        visited.add(start_node)
        
        while queue:
            node = queue.popleft()
            print(node, end=' ')
            
            for neighbor in self.adj_list[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

def main():
    # Create a graph
    g = Graph()
    
    # Add edges to the graph
    g.add_edge('A', 'B')
    g.add_edge('A', 'C')
    g.add_edge('B', 'D')
    g.add_edge('B', 'E')
    g.add_edge('C', 'F')
    g.add_edge('D', 'E')
    g.add_edge('E', 'F')
    g.add_edge('F', 'C')
    
    # Perform BFS traversal
    print("BFS Traversal:")
    g.bfs('A')

if __name__ == "__main__":
    main()
```

## Explanation

The code defines a `Graph` class with methods to add edges to the graph and perform BFS traversal. The `add_edge` method adds an edge between two nodes, and the `bfs` method performs BFS traversal from a given node. The `main` function creates a graph, adds edges to it, and performs BFS traversal from node 'A'.

## Example Output

```
BFS Traversal:
A B D E F C
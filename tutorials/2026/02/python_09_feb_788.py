# Breadth First Search (BFS) Graph Traversal in Python

from collections import deque

def create_graph(n_nodes):
    # Create an adjacency list to represent the graph
    graph = [[] for _ in range(n_nodes)]
    
    # Add edges to the graph
    for i in range(n_nodes - 1):
        graph[i].append(i + 1)
        graph[i + 1].append(i)
        
    return graph

def bfs_traversal(graph, start_node):
    # Create a visited set to keep track of visited nodes
    visited = set()
    
    # Create a queue for BFS, enqueue the start node
    queue = deque([start_node])
    
    # Mark the start node as visited
    visited.add(start_node)
    
    while queue:
        # Dequeue a node from the front of the queue
        node = queue.popleft()
        
        print(node, end=' ')
        
        # Enqueue all unvisited neighbors of the current node
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

# Create a graph with 6 nodes
n_nodes = 6
graph = create_graph(n_nodes)

# Perform BFS traversal starting from node 0
bfs_traversal(graph, 0)
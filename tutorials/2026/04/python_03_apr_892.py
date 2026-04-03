import sys
import heapq

def create_graph():
    # Create an empty graph as an adjacency list representation
    graph = {}
    return graph

def add_edge(graph, start, end, weight):
    # Add edge to the graph with its corresponding weight
    if start not in graph:
        graph[start] = []
    graph[start].append((end, weight))

def dijkstra(graph, start_node, end_node):
    # Create a priority queue to store nodes to be processed
    pq = [(0, start_node)]
    
    # Initialize distances and predecessors dictionaries
    distances = {node: float('infinity') for node in graph}
    predecessors = {node: None for node in graph}
    
    # Set the distance of the start node to 0
    distances[start_node] = 0
    
    while len(pq) > 0:
        # Extract the node with the minimum distance from the priority queue
        (dist, current_node) = heapq.heappop(pq)
        
        # If the extracted node is not the end node, update its neighbors' distances if possible
        for neighbor, weight in graph[current_node]:
            old_dist = distances[neighbor]
            new_dist = dist + weight
            
            # Update the distance and predecessor of the neighbor if a shorter path is found
            if new_dist < old_dist:
                distances[neighbor] = new_dist
                predecessors[neighbor] = current_node
                
                # Add the neighbor to the priority queue
                heapq.heappush(pq, (new_dist, neighbor))
                
    return distances, predecessors

def reconstruct_path(predecessors, end_node):
    # Reconstruct the shortest path from start node to end node
    path = []
    current_node = end_node
    
    while current_node is not None:
        path.append(current_node)
        current_node = predecessors[current_node]
        
    return path[::-1]

# Create a graph
graph = create_graph()

# Add edges to the graph with their corresponding weights
add_edge(graph, 'A', 'B', 2)
add_edge(graph, 'A', 'C', 4)
add_edge(graph, 'B', 'D', 3)
add_edge(graph, 'C', 'D', 1)
add_edge(graph, 'D', 'E', 5)

# Find the shortest path from node 'A' to node 'E'
distances, predecessors = dijkstra(graph, 'A', 'E')

# Reconstruct and print the shortest path
path = reconstruct_path(predecessors, 'E')
print("Shortest distance:", distances['E'])
print("Shortest path:", ' -> '.join(path))
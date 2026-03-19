# Dijkstra's Shortest Path Algorithm in Python

import sys
import heapq

def dijkstra(graph, start):
    # Create a dictionary to store the distance to each node
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    
    # Create a priority queue with the start node
    pq = [(0, start)]
    
    while pq:
        # Get the node with the smallest distance from the priority queue
        current_distance, current_node = heapq.heappop(pq)
        
        # If the current distance is greater than the stored distance, skip this node
        if current_distance > distances[current_node]:
            continue
        
        # Iterate over the neighbors of the current node
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            # If a shorter path to the neighbor is found, update its distance and push it back to the priority queue
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return distances

def main():
    # Define the graph as an adjacency list
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'D': 2, 'E': 5},
        'C': {'A': 4, 'F': 3},
        'D': {'B': 2, 'E': 1},
        'E': {'B': 5, 'D': 1, 'F': 1},
        'F': {'C': 3, 'E': 1}
    }
    
    # Define the start node
    start_node = 'A'
    
    # Run Dijkstra's algorithm
    distances = dijkstra(graph, start_node)
    
    # Print the shortest distances from the start node to all other nodes
    print("Shortest Distances:")
    for node, distance in distances.items():
        if distance == float('infinity'):
            print(f"{node}: Not reachable")
        else:
            print(f"{node}: {distance}")

if __name__ == "__main__":
    main()
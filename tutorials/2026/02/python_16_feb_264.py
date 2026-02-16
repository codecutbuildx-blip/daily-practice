# Dijkstra's Shortest Path Algorithm
#=====================================

import sys
import heapq

def dijkstra(graph, start):
    """
    This function implements Dijkstra's algorithm to find the shortest path from a given start node to all other nodes in a graph.
    
    Parameters:
    - graph (dict): A dictionary representing the adjacency list of the graph. Each key is a node and its corresponding value is another dictionary where keys are neighboring nodes and values are edge weights.
    - start (node): The node from which to start the search.

    Returns:
    - distances (dict): A dictionary containing the shortest distance from the start node to all other nodes in the graph. If an unreachable node exists, its distance will be infinity.
    - previous (dict): A dictionary where each key is a node and its corresponding value is the preceding node in the shortest path.
    """

    # Initialize distances and previous dictionaries
    distances = {node: sys.maxsize for node in graph}
    distances[start] = 0  # Distance to start node is 0

    # Create a priority queue containing all nodes with their initial distances
    pq = [(0, start)]

    while len(pq) > 0:
        current_distance, current_node = heapq.heappop(pq)

        # Process the current node
        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # If we find a shorter path to an adjacent node, update its distance and previous node
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))

    return distances, previous

# Example usage:
if __name__ == "__main__":
    # Define a graph as an adjacency list
    graph = {
        'A': {'B': 1, 'C': 3},
        'B': {'A': 1, 'C': 2, 'D': 4},
        'C': {'A': 3, 'B': 2, 'D': 5},
        'D': {'B': 4, 'C': 5}
    }

    start_node = 'A'

    distances, previous = dijkstra(graph, start_node)

    # Print the shortest distances from the start node to all other nodes
    print("Shortest Distances:")
    for node in graph:
        print(f"{start_node} -> {node}: {distances[node]}")

    # Reconstruct the shortest path using the previous dictionary
    print("\nPrevious Nodes:")
    current_node = 'D'
    while current_node != start_node:
        print(current_node, "->", previous[current_node])
        current_node = previous[current_node]

    print(f"{start_node} -> {current_node}: {distances[current_node]}")
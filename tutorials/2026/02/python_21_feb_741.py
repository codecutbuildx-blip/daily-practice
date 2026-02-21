# Topological Sort in Python

def topological_sort(graph):
    """
    Performs a topological sort on the given graph.
    
    Args:
    graph (dict): A dictionary representing the graph, where each key is a node and its corresponding value is a list of its neighbors.
    
    Returns:
    list: A list of nodes in topological order.
    """
    # Initialize a dictionary to store the in-degree of each node
    in_degree = {node: 0 for node in graph}
    
    # Calculate the in-degree of each node
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1
    
    # Initialize a queue to store nodes with in-degree 0
    queue = [node for node in in_degree if in_degree[node] == 0]
    
    # Initialize an empty list to store the sorted nodes
    sorted_nodes = []
    
    # Perform the topological sort
    while queue:
        node = queue.pop(0)
        sorted_nodes.append(node)
        
        # Decrease the in-degree of each neighbor by 1
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            
            # If the in-degree of a neighbor becomes 0, add it to the queue
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    # If there are nodes remaining in the graph, it means there's a cycle and the graph is not a DAG
    if len(sorted_nodes) != len(graph):
        raise ValueError("The graph contains a cycle and is not a Directed Acyclic Graph (DAG)")
    
    return sorted_nodes

# Example usage:
if __name__ == "__main__":
    # Define a graph as a dictionary
    graph = {
        'A': ['B', 'C'],
        'B': ['D'],
        'C': ['D'],
        'D': []
    }
    
    # Perform the topological sort
    sorted_nodes = topological_sort(graph)
    
    # Print the sorted nodes
    print("Topological Sort:")
    print(sorted_nodes)
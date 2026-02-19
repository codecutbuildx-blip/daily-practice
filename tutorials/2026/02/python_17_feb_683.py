class UnionFind:
    def __init__(self, n):
        # Initialize a list to store the parent of each element
        self.parent = list(range(n))
        
    def find(self, x):
        # If x is not its own parent, find its root and update the parent of x
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        # Find the roots of x and y
        root_x = self.find(x)
        root_y = self.find(y)
        
        # If they are not the same, merge them by making one parent of the other
        if root_x != root_y:
            self.parent[root_x] = root_y

# Example usage and test
if __name__ == "__main__":
    uf = UnionFind(6)  # Create a union-find object with 6 elements
    
    # Initially, each element is in its own set
    print("Initially:")
    for i in range(1, 7):
        print(f"{i} is in set {uf.find(i)}")
    
    # Merge sets 1 and 2
    uf.union(1, 2)
    print("\nAfter merging 1 and 2:")
    for i in range(1, 7):
        print(f"{i} is in set {uf.find(i)}")
    
    # Merge sets 3 and 4
    uf.union(3, 4)
    print("\nAfter merging 3 and 4:")
    for i in range(1, 7):
        print(f"{i} is in set {uf.find(i)}")
    
    # Try to merge a set with itself
    try:
        uf.union(5, 5)
    except ValueError:
        print("\nTrying to merge a set with itself raises an error.")
    else:
        print("This should not be executed.")
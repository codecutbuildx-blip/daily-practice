# Union-Find Data Structure
=====================================

This is an implementation of the Union-Find data structure in Python.

```python
class UnionFind:
    def __init__(self, size):
        """
        Initialize a new Union-Find object with the given size.
        
        Args:
            size (int): The number of elements in the set.
        """
        # Create a list to store the parent of each element
        self.parent = [i for i in range(size)]
        # Create a dictionary to store the rank of each element
        self.rank = {i: 0 for i in range(size)}

    def find(self, x):
        """
        Find the root of the set that contains x.
        
        Args:
            x (int): The element to find the root of.
        
        Returns:
            int: The root of the set that contains x.
        """
        # If the parent of x is not itself, then it's not in the correct set
        if self.parent[x] != x:
            # Recursively find the root and update the parent
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        """
        Union the sets that contain x and y.
        
        Args:
            x (int): The first element to union.
            y (int): The second element to union.
        """
        # Find the roots of the sets that contain x and y
        root_x = self.find(x)
        root_y = self.find(y)

        # If the roots are different, then we need to union them
        if root_x != root_y:
            # If the rank of root_x is less than the rank of root_y,
            # then root_y is the one that contains the other set
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            # If the ranks are equal, then we need to make root_x the new parent
            elif self.rank[root_x] == self.rank[root_y]:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1

# Example usage:
if __name__ == "__main__":
    uf = UnionFind(6)
    
    # Initially, each element is in its own set
    print("Initial parent:", uf.parent)
    
    # Union the sets that contain 0 and 1
    uf.union(0, 1)
    print("After union(0, 1):", uf.parent)
    
    # Find the root of the set that contains 2
    print("Find root of set containing 2:", uf.find(2))
    
    # Union the sets that contain 3 and 4
    uf.union(3, 4)
    print("After union(3, 4):", uf.parent)
    
    # Find the root of the set that contains 5
    print("Find root of set containing 5:", uf.find(5))
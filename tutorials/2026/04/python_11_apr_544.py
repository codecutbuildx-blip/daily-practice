# Union-Find Algorithm Implementation in Python
=============================================

## Overview

The Union-Find algorithm is a data structure that keeps track of a set of elements partitioned into disjoint subsets.

## Code

```python
class UnionFind:
    """
    A class representing the Union-Find algorithm.
    
    Attributes:
        parent (dict): A dictionary mapping each element to its parent.
        rank (dict): A dictionary mapping each element to its rank.
    """

    def __init__(self, size):
        """
        Initializes a new Union-Find instance with the given size.
        
        :param size: The number of elements in the sets.
        """
        self.parent = {i: i for i in range(size)}
        self.rank = {i: 0 for i in range(size)}

    def find(self, x):
        """
        Finds the root of the set containing element x.
        
        :param x: The element to find the root for.
        :return: The root of the set containing x.
        """
        if self.parent[x] != x:
            # Path compression optimization
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        """
        Merges the sets containing elements x and y.
        
        :param x: The first element to merge.
        :param y: The second element to merge.
        :return: True if the sets were merged, False otherwise.
        """
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            # Union by rank optimization
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            else:
                self.parent[root_x] = root_y
                if self.rank[root_x] == self.rank[root_y]:
                    self.rank[root_y] += 1
            return True
        return False

# Example usage
if __name__ == "__main__":
    # Create a Union-Find instance with 5 elements
    uf = UnionFind(5)

    # Merge some sets
    print("Merging sets:")
    uf.union(0, 1)  # [0, 1]
    uf.union(2, 3)  # [2, 3]
    uf.union(4, 0)  # [0, 1, 4]

    # Check the resulting set structure
    print("Finding roots:")
    print(uf.find(0))  # 0
    print(uf.find(1))  # 0
    print(uf.find(2))  # 2
    print(uf.find(3))  # 2
    print(uf.find(4))  # 4

    # Check that no more merges are possible
    print("Checking for mergeability:")
    print(uf.union(0, 2))  # False
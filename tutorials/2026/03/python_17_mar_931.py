# Heap Operations in Python
import heapq

class MinHeap:
    def __init__(self):
        self.heap = []

    # Insert an element into the heap
    def insert(self, value):
        # Add the element to the end of the list
        heapq.heappush(self.heap, value)

    # Remove and return the smallest element from the heap
    def get_min(self):
        # Check if the heap is empty
        if not self.heap:
            raise ValueError("Heap is empty")
        # Return the first element (smallest) of the heap
        return self.heap[0]

    # Delete an element from the heap
    def delete(self, value):
        # Check if the element exists in the heap
        try:
            # Get the index of the element to be deleted
            index = self.heap.index(value)
            # Remove and replace the element with the last element in the list
            self.heap[index] = self.heap[-1]
            # Remove the last element from the list
            del self.heap[-1]
            # Heapify the list (rebuild the heap property)
            self._heapify()
        except ValueError:
            print("Element not found")

    def _heapify(self):
        # Start from the root node and compare with its children
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            # Compare the current element with its left child
            if i * 2 + 1 < len(self.heap) and self.heap[i] > self.heap[i * 2 + 1]:
                # Swap the elements
                self.heap[i], self.heap[i * 2 + 1] = self.heap[i * 2 + 1], self.heap[i]
            # Compare the current element with its right child
            if i * 2 + 2 < len(self.heap) and self.heap[i] > self.heap[i * 2 + 2]:
                # Swap the elements
                self.heap[i], self.heap[i * 2 + 2] = self.heap[i * 2 + 2], self.heap[i]

    def size(self):
        return len(self.heap)

    def is_empty(self):
        return not self.heap

# Example usage:
min_heap = MinHeap()
print("Initial heap:", min_heap.heap)
min_heap.insert(5)
min_heap.insert(3)
min_heap.insert(8)
min_heap.insert(1)
min_heap.insert(2)
min_heap.insert(7)

print("Smallest element:", min_heap.get_min())  # Output: 1
print("Heap size:", min_heap.size())  # Output: 6

min_heap.delete(5)
print("Heap after deletion:", min_heap.heap)

if not min_heap.is_empty():
    print("Heap is not empty")
else:
    print("Heap is empty")
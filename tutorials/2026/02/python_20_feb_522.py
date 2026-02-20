# Heap Operations in Python

# Importing necessary libraries
import heapq

# Heap Operations

# Creating a min heap
def create_min_heap():
    # Initialize a list to represent the heap
    heap = [4, 2, 9, 6, 5, 1, 8, 3, 7]
    # Heapify the list to create a min heap
    heapq.heapify(heap)
    return heap

# Heapify a list to create a min heap
def heapify(lst):
    # Start from the last non-leaf node and perform heapify operation
    for i in range(len(lst) // 2 - 1, -1, -1):
        # Heapify the subtree rooted at index i
        _heapify(lst, i)

def _heapify(lst, i):
    # Initialize the smallest element as the root
    smallest = i
    # Calculate the left and right child indices
    left = 2 * i + 1
    right = 2 * i + 2
    # If the left child is smaller than the root, update the smallest element
    if left < len(lst) and lst[left] < lst[smallest]:
        smallest = left
    # If the right child is smaller than the smallest element, update the smallest element
    if right < len(lst) and lst[right] < lst[smallest]:
        smallest = right
    # If the smallest element is not the root, swap them
    if smallest != i:
        lst[i], lst[smallest] = lst[smallest], lst[i]
        # Recursively heapify the affected subtree
        _heapify(lst, smallest)

# Extract the minimum element from the heap
def extract_min(heap):
    # If the heap is empty, raise an exception
    if len(heap) == 0:
        raise Exception("Heap is empty")
    # The minimum element is the first element in the heap
    min_element = heap[0]
    # Swap the minimum element with the last element in the heap
    heap[0] = heap[-1]
    # Remove the last element from the heap
    heap.pop()
    # Heapify the heap to maintain the heap property
    heapq.heapify(heap)
    return min_element

# Insert an element into the heap
def insert(heap, element):
    # Add the element to the end of the heap
    heapq.heappush(heap, element)

# Example usage
if __name__ == "__main__":
    # Create a min heap
    min_heap = create_min_heap()
    print("Min Heap:", min_heap)

    # Insert elements into the heap
    insert(min_heap, 10)
    insert(min_heap, 20)
    insert(min_heap, 15)
    insert(min_heap, 30)
    insert(min_heap, 25)

    # Extract the minimum element from the heap
    print("Extracted Minimum Element:", extract_min(min_heap))

    # Print the updated heap
    print("Updated Min Heap:", min_heap)
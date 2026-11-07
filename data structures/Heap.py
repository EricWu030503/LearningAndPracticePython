"""
Heap Data Structure (Min-Heap / Max-Heap)
=========================================

A Heap is a special tree-based data structure that satisfies the **heap property**:

    - In a **Min-Heap**, the value of each node is **less than or equal to** the values of its children.
    - In a **Max-Heap**, the value of each node is **greater than or equal to** the values of its children.

This property makes heaps useful for efficiently implementing **priority queues**, **sorting algorithms** (like heapsort),
and solving problems where repeatedly extracting the minimum or maximum is required (e.g., Dijkstra’s algorithm).

Heap Characteristics:
---------------------
- Typically implemented as a **complete binary tree**:
    - Every level is fully filled except possibly the last.
    - The last level is filled from **left to right**.

- Heaps can be implemented in two common ways:
    1. **Array-based Binary Heap**:
        - Uses a list or array to store the tree.
        - For any element at index `i`:
            - Left child:  `2 * i + 1`
            - Right child: `2 * i + 2`
            - Parent:      `(i - 1) // 2`
        - Allows O(log n) insertion and extraction.

    2. **Pointer-based Binary Tree**:
        - Each node explicitly stores links to left, right, and parent nodes.
        - More flexible structurally, but less cache-friendly than array-based implementation.

Heap Operations:
----------------
- `insert(value)`:
    Adds a new value and maintains the heap property by bubbling up.

- `extract()`:
    Removes and returns the root (min or max), then restores the heap by bubbling down.

- `peek()`:
    Returns the root value without removing it.

- `is_empty()` / `size()`:
    Utility functions to query the state of the heap.

Time Complexity:
----------------
- Insertion:       O(log n)
- Extraction:      O(log n)
- Peek (get min/max): O(1)

This module implements the Heap ADT using both array-based and pointer-based structures,
demonstrating the core operations and maintaining a min-heap property.
"""


from abc import ABC, abstractmethod

class Heap(ABC):
    @abstractmethod
    def insert(self, value):
        pass  # Insert a value into the heap

    @abstractmethod
    def extract(self):
        pass  # Extract the root (max/min) element

    @abstractmethod
    def peek(self):
        pass  # Peek at the root element without removing it

    @abstractmethod
    def size(self):
        pass  # Return the number of elements in the heap

    @abstractmethod
    def is_empty(self):
        pass  # Check if the heap is empty


class ArrayHeap(Heap):
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)  # Add to the end of the array
        self._bubble_up(len(self.heap) - 1)  # Restore the heap property

    def extract(self):
        if self.is_empty():
            raise IndexError("Heap is empty")
        root = self.heap[0]  # The root element
        last = self.heap.pop()  # Remove the last element
        if not self.is_empty():
            self.heap[0] = last  # Move the last element to the root
            self._bubble_down(0)  # Restore the heap property
        return root

    def peek(self):
        if self.is_empty():
            raise IndexError("Heap is empty")
        return self.heap[0]

    def size(self):
        return len(self.heap)

    def is_empty(self):
        return len(self.heap) == 0

    # Restore heap property after insertion
    def _bubble_up(self, index):
        parent = (index - 1) // 2
        while index > 0 and self.heap[index] < self.heap[parent]:
            self._swap(index, parent)
            index = parent
            parent = (index - 1) // 2

    # Restore heap property after extraction
    def _bubble_down(self, index):
        left_child = 2 * index + 1
        right_child = 2 * index + 2
        smallest = index

        if left_child < len(self.heap) and self.heap[left_child] < self.heap[smallest]:
            smallest = left_child
        if right_child < len(self.heap) and self.heap[right_child] < self.heap[smallest]:
            smallest = right_child
        if smallest != index:
            self._swap(index, smallest)
            self._bubble_down(smallest)

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

class BinaryTreeHeap(Heap):
    class Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None
            self.parent = None

    def __init__(self):
        self.root = None
        self._size = 0

    def insert(self, value):
        new_node = self.Node(value)
        if self.root is None:
            self.root = new_node
        else:
            parent = self._find_parent(self._size + 1)  # Find the parent of the next insertion point
            if parent.left is None:
                parent.left = new_node
            else:
                parent.right = new_node
            new_node.parent = parent
            self._bubble_up(new_node)  # Restore heap property
        self._size += 1

    def extract(self):
        if self.is_empty():
            raise IndexError("Heap is empty")
        root_value = self.root.value

        if self._size == 1:
            self.root = None
        else:
            last_node = self._find_node(self._size)  # Find the last node
            self.root.value = last_node.value  # Move last node's value to root
            if last_node.parent.right == last_node:
                last_node.parent.right = None
            else:
                last_node.parent.left = None
            self._bubble_down(self.root)  # Restore heap property
        self._size -= 1
        return root_value

    def peek(self):
        if self.is_empty():
            raise IndexError("Heap is empty")
        return self.root.value

    def size(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    # Restore heap property after insertion
    def _bubble_up(self, node):
        while node.parent is not None and node.value < node.parent.value:
            self._swap(node, node.parent)
            node = node.parent

    # Restore heap property after extraction
    def _bubble_down(self, node):
        while node is not None:
            smallest = node
            if node.left is not None and node.left.value < smallest.value:
                smallest = node.left
            if node.right is not None and node.right.value < smallest.value:
                smallest = node.right
            if smallest != node:
                self._swap(node, smallest)
                node = smallest
            else:
                break

    def _swap(self, a, b):
        a.value, b.value = b.value, a.value

    # Find the parent of the next insertion point (1-based index)
    def _find_parent(self, index):
        path = bin(index)[3:]  # Binary path to the node
        current = self.root
        for direction in path[:-1]:
            current = current.left if direction == '0' else current.right
        return current

    # Find the node at a specific 1-based index
    def _find_node(self, index):
        path = bin(index)[3:]  # Binary path to the node
        current = self.root
        for direction in path:
            current = current.left if direction == '0' else current.right
        return current

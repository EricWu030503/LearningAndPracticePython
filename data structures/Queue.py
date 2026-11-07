from typing import Any

# ArrayQueue: circular array-based queue
class ArrayQueue:
    def __init__(self, capacity):
        self.queue = [None] * capacity
        self.front = 0
        self.rear = -1
        self.size = 0

    # Time complexity: O(1)
    def enqueue(self, element):
        if self.size == len(self.queue):
            raise Exception("Queue is full")
        self.rear = (self.rear + 1) % len(self.queue)
        self.queue[self.rear] = element
        self.size += 1

    # Time complexity: O(1)
    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        element = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1) % len(self.queue)
        self.size -= 1
        return element

    # Time complexity: O(1)
    def peek(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.queue[self.front]

    # Time complexity: O(1)
    def is_empty(self):
        return self.size == 0

    # Time complexity: O(1)
    def is_full(self):
        return self.size == len(self.queue)


# LinkedListQueue: using DLList from List.py (assume it's imported as DLList)
class DLListQueue:
    def __init__(self):
        from List import DLList  # local import to respect user structure
        self.queue = DLList()

    # Time complexity: O(1)
    def enqueue(self, x: Any):
        self.queue.add_last(x)

    # Time complexity: O(1)
    def dequeue(self) -> Any:
        return self.queue.remove_first()

    # Time complexity: O(1)
    def peek(self) -> Any:
        return self.queue.get_first()

    # Time complexity: O(1)
    def is_empty(self) -> bool:
        return self.queue.size == 0


# TwoStackQueue: using two stacks from Stack.py (assume it's using ArrayStack)
class TwoStackQueue:
    def __init__(self):
        from Stack import ArrayStack
        self.in_stack = ArrayStack(100)
        self.out_stack = ArrayStack(100)

    # Time complexity: O(1) amortized
    def enqueue(self, x: Any):
        self.in_stack.push(x)

    # Time complexity: O(1) amortized
    def dequeue(self) -> Any:
        if self.out_stack.empty():
            while not self.in_stack.empty():
                self.out_stack.push(self.in_stack.pop())
        return self.out_stack.pop()

    # Time complexity: O(1) amortized
    def peek(self) -> Any:
        if self.out_stack.empty():
            while not self.in_stack.empty():
                self.out_stack.push(self.in_stack.pop())
        return self.out_stack.top_element()

    # Time complexity: O(1)
    def is_empty(self) -> bool:
        return self.in_stack.empty() and self.out_stack.empty()

class ArrayList:
    def __init__(self):
        self.items = [None] * 100
        self.size = 0

    # Time complexity: O(n)
    def _resize(self, capacity):
        new_items = [None] * capacity
        for i in range(self.size):
            new_items[i] = self.items[i]
        self.items = new_items

    # Time complexity: O(n)
    def add_first(self, x):
        self.insert(x, 0)

    # Amortized time complexity: O(1)
    def add_last(self, x):
        if self.size == len(self.items):
            self._resize(self.size * 2)
        self.items[self.size] = x
        self.size += 1

    # Time complexity: O(1)
    def get_first(self):
        return self.items[0]

    # Time complexity: O(1)
    def get_last(self):
        return self.items[self.size - 1]

    # Time complexity: O(1)
    def get(self, i):
        return self.items[i]

    # Time complexity: O(1)
    def remove_last(self):
        x = self.get_last()
        self.items[self.size - 1] = None
        self.size -= 1
        return x

    # Time complexity: O(n)
    def insert(self, x, position):
        if position < 0 or position > self.size:
            raise IndexError("Invalid position")
        if self.size == len(self.items):
            self._resize(self.size * 2)
        for i in range(self.size, position, -1):
            self.items[i] = self.items[i - 1]
        self.items[position] = x
        self.size += 1

    # Time complexity: O(n)
    def print(self):
        for i in range(self.size):
            print(self.items[i], end=" ")
        print()

class SLList:
    class Node:
        def __init__(self, item, next_node=None):
            self.item = item
            self.next = next_node

    def __init__(self):
        self.sentinel = self.Node(None)
        self.size = 0

    # Time complexity: O(1)
    def add_first(self, x):
        self.sentinel.next = self.Node(x, self.sentinel.next)
        self.size += 1

    # Time complexity: O(1)
    def get_first(self):
        return self.sentinel.next.item

    # Time complexity: O(n)
    def add_last(self, x):
        p = self.sentinel
        while p.next:
            p = p.next
        p.next = self.Node(x)
        self.size += 1

    # Time complexity: O(n)
    def get_last(self):
        p = self.sentinel
        while p.next:
            p = p.next
        return p.item

    # Time complexity: O(n)
    def remove_last(self):
        if self.size == 0:
            return None
        p = self.sentinel
        while p.next.next:
            p = p.next
        last_item = p.next.item
        p.next = None
        self.size -= 1
        return last_item

    # Time complexity: O(n)
    def get(self, i):
        p = self.sentinel.next
        for _ in range(i):
            p = p.next
        return p.item

    # Time complexity: O(n)
    def print(self):
        p = self.sentinel.next
        while p:
            print(p.item, end=" ")
            p = p.next
        print()

class DLList:
    class Node:
        def __init__(self, item, prev=None, next_node=None):
            self.item = item
            self.prev = prev
            self.next = next_node

    def __init__(self):
        self.sentinel = self.Node(None)
        self.sentinel.prev = self.sentinel
        self.sentinel.next = self.sentinel
        self.size = 0

    # Time complexity: O(1)
    def add_first(self, item):
        new_node = self.Node(item, self.sentinel, self.sentinel.next)
        self.sentinel.next.prev = new_node
        self.sentinel.next = new_node
        self.size += 1

    # Time complexity: O(1)
    def add_last(self, item):
        new_node = self.Node(item, self.sentinel.prev, self.sentinel)
        self.sentinel.prev.next = new_node
        self.sentinel.prev = new_node
        self.size += 1

    # Time complexity: O(1)
    def remove_first(self):
        if self.size == 0:
            return None
        first = self.sentinel.next
        self.sentinel.next = first.next
        first.next.prev = self.sentinel
        self.size -= 1
        return first.item

    # Time complexity: O(1)
    def remove_last(self):
        if self.size == 0:
            return None
        last = self.sentinel.prev
        self.sentinel.prev = last.prev
        last.prev.next = self.sentinel
        self.size -= 1
        return last.item

    # Time complexity: O(1)
    def get_first(self):
        return self.sentinel.next.item if self.size > 0 else None

    # Time complexity: O(1)
    def get_last(self):
        return self.sentinel.prev.item if self.size > 0 else None

    # Time complexity: O(1)
    def size(self):
        return self.size

    # Time complexity: O(n)
    def print(self):
        p = self.sentinel.next
        while p != self.sentinel:
            print(p.item, end=" ")
            p = p.next
        print()

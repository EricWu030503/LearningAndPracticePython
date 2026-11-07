class ArrayStack:
    def __init__(self, capacity):
        self.stack = [0] * capacity
        self.top = -1

    def empty(self):  # O(1)
        return self.top == -1

    def push(self, element):  # O(1)
        if self.top == len(self.stack) - 1:
            raise OverflowError("Stack is full")
        self.top += 1
        self.stack[self.top] = element

    def top_element(self):  # O(1)
        if self.empty():
            raise IndexError("Stack is empty")
        return self.stack[self.top]

    def pop(self):  # O(1)
        if self.empty():
            raise IndexError("Stack is empty")
        element = self.stack[self.top]
        self.top -= 1
        return element


class LinkedListStack:
    class Node:
        def __init__(self, value, next_node=None):
            self.value = value
            self.next = next_node

    def __init__(self):
        self.head = None

    def empty(self):  # O(1)
        return self.head is None

    def push(self, element):  # O(1)
        self.head = self.Node(element, self.head)

    def top_element(self):  # O(1)
        if self.empty():
            raise IndexError("Stack is empty")
        return self.head.value

    def pop(self):  # O(1)
        if self.empty():
            raise IndexError("Stack is empty")
        value = self.head.value
        self.head = self.head.next
        return value


def main():
    print("=== ArrayStack Demo ===")
    array_stack = ArrayStack(5)
    array_stack.push(10)
    array_stack.push(20)
    array_stack.push(30)
    print("Top element:", array_stack.top_element())  # Should print 30
    array_stack.pop()
    print("Top after pop:", array_stack.top_element())  # Should print 20
    print("Is empty?", array_stack.empty())  # Should print False

    print("\n=== LinkedListStack Demo ===")
    linked_stack = LinkedListStack()
    linked_stack.push(100)
    linked_stack.push(200)
    linked_stack.push(300)
    print("Top element:", linked_stack.top_element())  # Should print 300
    linked_stack.pop()
    print("Top after pop:", linked_stack.top_element())  # Should print 200
    print("Is empty?", linked_stack.empty())  # Should print False

    print("\n=== Python List Stack Demo ===")
    stack = []
    stack.append("a")
    stack.append("b")
    stack.append("c")
    print("Top element:", stack[-1])  # Should print 'c'
    stack.pop()
    print("Top after pop:", stack[-1])  # Should print 'b'
    print("Is empty?", len(stack) == 0)  # Should print False
    # In practice we will only use python list to simulate stack operations

if __name__ == "__main__":
    main()

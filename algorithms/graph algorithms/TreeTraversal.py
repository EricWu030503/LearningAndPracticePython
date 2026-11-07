class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class TreeTraversal:
    def __init__(self):
        self.root = None

    def in_order_traversal(self, node):
        if node:
            self.in_order_traversal(node.left)
            self.visit(node)  # Placeholder for visit operation (e.g., print node value)
            self.in_order_traversal(node.right)

    def pre_order_traversal(self, node):
        if node:
            self.visit(node)  # Placeholder for visit operation
            self.pre_order_traversal(node.left)
            self.pre_order_traversal(node.right)

    def post_order_traversal(self, node):
        if node:
            self.post_order_traversal(node.left)
            self.post_order_traversal(node.right)
            self.visit(node)  # Placeholder for visit operation

    def visit(self, node):
        print(node.value)


# Main function to test the tree traversals
if __name__ == "__main__":
    tree = TreeTraversal()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)

    print("In-order traversal:")
    tree.in_order_traversal(tree.root)

    print("\nPre-order traversal:")
    tree.pre_order_traversal(tree.root)

    print("\nPost-order traversal:")
    tree.post_order_traversal(tree.root)

# note that these 3 types of traversals are indeed DFS algorithm
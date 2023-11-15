class TreeNode:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None

    def parse_tuple(self,data):
        if isinstance(data,tuple) and len(data)==3:
            node=TreeNode(data[1])
            node.left=self.parse_tuple(data[0])
            node.right=self.parse_tuple(data[2])
        elif data is None:
            node=None
        else:
            node=self(data)
        return node

    def traverse_inorder(self,node):
        if node is None:
            return []
        return self.traverse_inorder(node.left)+[node.key]+self.traverse_inorder(node.right)

    def tree_height(self,node):
        if node is None:
            return 0
        return 1+max(self.tree_height(node.left),self.tree_height(node.right))

    def tree_size(self,node):
        if node is None:
            return 0
        return 1+self.tree_size(node.left)+self.tree_size(node.right)

tree_tuple=((1,3,None),2,((None,3,4),5,(6,7,8)))
tree=TreeNode.parse_tuple(tree_tuple)
print(TreeNode.traverse_inorder(tree))














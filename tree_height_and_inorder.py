class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

class BinaryTree:
    def inorder_traversal(self, root):
        if root is None:
            return
        self.inorder_traversal(root.left)
        print(root.data, end=" ")
        self.inorder_traversal(root.right)

    def height(self, root):
        if root is None:
            return 0
        return 1 + max(self.height(root.left), self.height(root.right))

root = Node(5)
root.left = Node(6)
root.right = Node(12)
root.right.right = Node(3)
root.left.left = Node(10)
root.left.right = Node(33)
root.left.left.left = Node(56)

obj = BinaryTree()
obj.inorder_traversal(root)
print()
print("Height of the tree:", obj.height(root))

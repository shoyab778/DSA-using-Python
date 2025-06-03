class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

def preorder_traversal(root):
    if root is None:
        return
    print(root.data, end=" ")
    preorder_traversal(root.left)
    preorder_traversal(root.right)

root = Node(5)
root.left = Node(6)
root.right = Node(12)
root.left.left = Node(10)
root.left.right = Node(33)
root.left.left.left = Node(56)
root.right.right = Node(3)

preorder_traversal(root)

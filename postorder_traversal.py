class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

def postorder_traversal(root):
    if root is None:
        return
    postorder_traversal(root.left)
    postorder_traversal(root.right)
    print(root.data, end=" ")

root = Node(5)
root.left = Node(6)
root.right = Node(12)
root.left.left = Node(10)
root.left.right = Node(33)
root.left.left.left = Node(56)
root.right.right = Node(3)

postorder_traversal(root)

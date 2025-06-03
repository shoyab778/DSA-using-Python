class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class bst:
    def __init__(self):
        self.root = None
    def insert(self, data):
        self.root = self.rec_insert(self.root, data)
    def rec_insert(self, root, data):
        if root is None:
            return Node(data)
        if root.data > data:
            root.left = self.rec_insert(root.left, data)
        else:
            root.right = self.rec_insert(root.right, data)
        return root
    def inorder(self):
        def rec_inorder(root):
            if root:
                rec_inorder(root.left)
                print(root.data, end=" ")
                rec_inorder(root.right)
        rec_inorder(self.root)
    def sum(self, root):
        if not root:
            return 0
        return root.data + self.sum(root.left) + self.sum(root.right)
    def count(self, root):
        if not root:
            return 0
        return 1 + self.count(root.left) + self.count(root.right)
    def height(self, root):
        if not root:
            return 0
        return 1 + max(self.height(root.left), self.height(root.right))
    def left_sum(self, root):
        if root is None:
            return 0
        total = 0
        if root.left:
            total += root.left.data
        total += self.left_sum(root.left)
        total += self.left_sum(root.right)
        return total
    def min(self, root):
        if root is None:
            print("no data")
            return None
        while root.left:
            root = root.left
        return root.data
    def max(self, root):
        if root is None:
            print("no data")
            return None
        while root.right:
            root = root.right
        return root.data

obj = bst()
obj.insert(20)
obj.insert(60)
obj.insert(70)
obj.insert(5)
obj.insert(351)
obj.insert(10)
obj.inorder()
print()
print(obj.max(obj.root))

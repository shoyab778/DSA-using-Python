def find(self, root, key):
    if root is None or root.data == key:
        return root
    if key < root.data:
        return self.find(root.left, key)
    else:
        return self.find(root.right, key)

def delete(self, root, key):
    if root:
        if root.data > key:
            root.left = self.delete(root.left, key)
            return root
        elif root.data < key:
            root.right = self.delete(root.right, key)
            return root
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        max_val = self.max(root.left)
        root.data=max_val
        self.delete(root.left,max_val)
        return root

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def b_insert(self, data):
        newnode = Node(data)
        newnode.next = self.head
        self.head = newnode

    def e_insert(self, data):
        newnode = Node(data)
        if not self.head:
            self.head = newnode
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = newnode

    def b_delete(self):
        if self.head:
            self.head = self.head.next

    def display(self):
        if not self.head:
            print("empty")
            return
        cur = self.head
        while cur:
            print(cur.data, end="->")
            cur = cur.next

obj = LinkedList()
obj.b_insert(8)
obj.b_insert(10)
obj.e_insert(36)
obj.display()
print()
obj.b_delete()
obj.display()

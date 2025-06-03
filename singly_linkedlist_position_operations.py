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

    def e_delete(self):
        if not self.head or not self.head.next:
            self.head = None
            return
        cur = self.head
        while cur.next.next:
            cur = cur.next
        cur.next = None

    def position(self, pos):
        if pos <= 0:
            return None
        cur = self.head
        for _ in range(pos - 1):
            if cur and cur.next:
                cur = cur.next
            else:
                return None
        return cur

    def pos_insert(self, data, pos):
        if pos == 1:
            self.b_insert(data)
            return
        cur = self.position(pos - 1)
        if cur:
            newnode = Node(data)
            newnode.next = cur.next
            cur.next = newnode
        else:
            print("Position not found")

    def pos_delete(self, pos):
        if pos == 1:
            self.b_delete()
            return
        cur = self.position(pos - 1)
        if cur and cur.next:
            cur.next = cur.next.next
        else:
            print("Position not found")

    def display(self):
        if not self.head:
            print("empty")
            return
        cur = self.head
        while cur:
            print(cur.data, end="->")
            cur = cur.next

obj = LinkedList()
obj.b_insert(10)
obj.e_insert(8)
obj.e_insert(36)
obj.display()
print()
obj.pos_delete(4)
obj.display()

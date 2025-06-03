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
        if self.head is None:
            self.head = newnode
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = newnode

    def display(self):
        if self.head is None:
            print("Empty")
            return
        cur = self.head
        while cur:
            print(cur.data, end="->")
            cur = cur.next
        print("None")


if __name__ == "__main__":
    ll = LinkedList()
    ll.b_insert(8)
    ll.b_insert(10)
    ll.b_insert(21)
    ll.e_insert(36)
    ll.display()

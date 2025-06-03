class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linked_list:
    def __init__(self):
        self.head = None

    def e_insert(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = newnode

    def remove_dup(self):
        cur = self.head
        while cur and cur.next:
            if cur.data == cur.next.data:
                cur.next = cur.next.next
            else:
                cur = cur.next

    def display(self):
        if self.head is None:
            print("empty")
            return
        cur = self.head
        while cur:
            print(cur.data, end="->")
            cur = cur.next
        print()

t = int(input("Enter number of test cases: "))
obj = [0] * t
for i in range(t):
    obj[i] = Linked_list()
    n = int(input("Enter number of elements: "))
    a = list(map(int, input("Enter elements: ").split()))
    for j in range(n):
        obj[i].e_insert(a[j])
    obj[i].remove_dup()

for k in obj:
    k.display()

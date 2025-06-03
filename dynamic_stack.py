class Stack:
    def __init__(self):
        self.box = []

    def push(self, data):
        self.box.append(data)

    def pop(self):
        if len(self.box) == 0:
            print("Empty")
            return
        self.box.pop()

    def peek(self):
        if len(self.box) == 0:
            print("Empty")
            return
        print(self.box[-1])

    def display(self):
        if len(self.box) == 0:
            print("Empty")
            return
        for i in reversed(self.box):
            print(i, end=" ")
        print()


if __name__ == "__main__":
    stack1 = Stack()
    stack1.push(18)
    stack1.push(7)
    stack1.display()
    stack1.pop()
    stack1.pop()
    stack1.display()

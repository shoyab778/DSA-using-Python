class Stack:
    def __init__(self, size):
        self.size = size
        self.box = [0] * self.size
        self.top = -1

    def push(self, data):
        if self.top + 1 == self.size:
            print("Overflow")
            return
        self.top += 1
        self.box[self.top] = data

    def pop(self):
        if self.top == -1:
            print("Underflow")
            return
        self.top -= 1

    def peek(self):
        if self.top == -1:
            print("Underflow")
            return
        print(self.box[self.top])

    def display(self):
        if self.top == -1:
            print("Underflow")
            return
        for i in range(self.top, -1, -1):
            print(self.box[i], end=" ")
        print()


if __name__ == "__main__":
    stack1 = Stack(3)
    stack1.push(18)
    stack1.push(7)
    stack1.display()
    stack1.pop()
    stack1.pop()
    stack1.display()

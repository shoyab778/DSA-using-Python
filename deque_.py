class Deque:
    def __init__(self, size):
        self.size = size
        self.front = self.rear = -1
        self.queue = [0] * self.size

    def enqueue(self, data):
        if self.rear == -1:
            self.front = self.rear = 0
            self.queue[self.rear] = data
        elif self.rear + 1 == self.size:
            print("Full")
        else:
            self.rear += 1
            self.queue[self.rear] = data

    def dequeue(self):
        if self.front == -1 or self.front > self.rear:
            print("Empty")
            return
        self.front += 1

    def front_element(self):
        if self.front == -1 or self.front > self.rear:
            print("Empty")
            return
        print(self.queue[self.front])

    def display(self):
        if self.front == -1 or self.front > self.rear:
            print("Empty")
            return
        for i in range(self.front, self.rear + 1):
            print(self.queue[i], end=" ")
        print()


if __name__ == "__main__":
    d = Deque(3)
    d.enqueue(18)
    d.enqueue(7)
    d.display()
    d.dequeue()
    d.display()

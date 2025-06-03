class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if not self.queue:
            print("Empty")
            return
        self.queue.pop(0)

    def front(self):
        if not self.queue:
            print("Empty")
            return
        print(self.queue[0])

    def display(self):
        if not self.queue:
            print("Empty")
            return
        for item in self.queue:
            print(item, end=" ")
        print()


if __name__ == "__main__":
    q = Queue()
    q.enqueue(18)
    q.enqueue(7)
    q.display()
    q.dequeue()
    q.display()

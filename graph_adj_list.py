class Graph:
    def __init__(self):
        self.graph = {}

    def insert(self, v, e):
        if v not in self.graph:
            self.graph[v] = [e]
        else:
            self.graph[v].append(e)

obj = Graph()
obj.insert("B", "T")  # from B to T
obj.insert("T", "B")
obj.insert("B", "P")
obj.insert("P", "B")
obj.insert("D", "P")
obj.insert("P", "D")
obj.insert("D", "T")
obj.insert("T", "D")
obj.insert("B", "L")
obj.insert("L", "B")

print(obj.graph)

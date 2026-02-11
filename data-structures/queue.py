class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)
    
queue = Queue()

print(queue.isEmpty())

queue.enqueue("ankara")
queue.enqueue("istanbul")
print(queue.size())

queue.dequeue()
print(queue.size())

queue.dequeue()
print(queue.size())
print(queue.isEmpty())
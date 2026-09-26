# Implementation of queue using array.

class Queue:

    def __init__(self):
        self.queue = []

    def enqueue(self, element):
        self.queue.append(element)

    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty!"
        return self.queue.pop(0)

    def peek(self):
        if self.isEmpty():
            return "Queue is empty!"
        return self.queue[0]

    def isEmpty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

my_queue = Queue()

my_queue.enqueue("A")
my_queue.enqueue("B")
my_queue.enqueue("C")
my_queue.enqueue("D")
my_queue.enqueue("E")

print(f"My Queue: {my_queue.queue}")

print(f"Dequeue: {my_queue.dequeue()}")

print(f"Peek: {my_queue.peek()}")

print(f"Empty: {my_queue.isEmpty()}")

print(f"Size: {my_queue.size()}")
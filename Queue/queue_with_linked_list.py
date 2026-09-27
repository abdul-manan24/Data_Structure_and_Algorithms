# Implementation of queue with linked list.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:

    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def enqueue(self, element):
        new_node = Node(element)
        if self.rear == None:
            self.front = self.rear = new_node
            self.size += 1
        self.rear.next = new_node
        self.rear = new_node
        self.size += 1

    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        temp = self.front
        self.front = temp.next
        self.size -= 1
        if self.front is None:
            self.rear = None
        return temp.data

    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.front.data

    def isEmpty(self):
        return self.size == 0

    def queueSize(self):
        return self.size

    def traverseAndPrint(self):
        current_node = self.front

        while current_node:
            print(current_node.data, end=" ")
            current_node = current_node.next
        print("null")

my_queue = Queue()

my_queue.enqueue("A")
my_queue.enqueue("B")
my_queue.enqueue("C")
my_queue.enqueue("D")
my_queue.enqueue("E")

my_queue.traverseAndPrint()

print(f"Dequeue: {my_queue.dequeue()}")

print(f"Peek: {my_queue.peek()}")

print(f"Empty: {my_queue.isEmpty()}")

print(f"Size of queue: {my_queue.queueSize()}")
# Implementation of stack using linked list.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:

    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, element):
        new_node = Node(element)

        if self.head:
            new_node.next = self.head

        self.head = new_node
        self.size += 1
        
    def pop(self):
        if self.isEmpty():
            return "Stack is empty!"
        popped_node = self.head
        self.head = self.head.next
        self.size -= 1
        return popped_node.data

    def peek(self):
        if self.isEmpty():
            return "Stack is empty!"

        return self.head.data

    def isEmpty(self):
        return self.size == 0

    def stack_size(self):
        return self.size

    def traverse_and_print(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("null")

my_stack = Stack()

my_stack.push("A")
my_stack.push("B")
my_stack.push("C")
my_stack.push("D")
my_stack.push("E")

my_stack.traverse_and_print()

print(f"Pop: {my_stack.pop()}")

print(f"Peek: {my_stack.peek()}")

print(f"Empty: {my_stack.isEmpty()}")

print(f"Size: {my_stack.stack_size()}")
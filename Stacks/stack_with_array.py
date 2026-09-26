# Implementation of stack using array.

class Stack:

    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack.pop()

    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack[-1]

    def isEmpty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

my_stack = Stack()

my_stack.push("A")
my_stack.push("B")
my_stack.push("C")
my_stack.push("D")
my_stack.push("E")

print(f"Stack: {my_stack.stack}")

print(f"Pop: {my_stack.pop()}")

print(f"Peek: {my_stack.peek()}")

print(f"Empty: {my_stack.isEmpty()}")

print(f"Size: {my_stack.size()}")
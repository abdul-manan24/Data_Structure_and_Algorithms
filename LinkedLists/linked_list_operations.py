# In this code i am going to insert and delete a node in linked list.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

node1 = Node(3)
node2 = Node(5)
node3 = Node(14)
node4 = Node(2)
node5 = Node(12)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

def traverseAndPrint(head):

    currentNode = head
    startNode = head
    print(currentNode.data, end=" -> ")
    currentNode = currentNode.next

    while currentNode:
        print(currentNode.data, end=" -> ")
        currentNode = currentNode.next
    print("Null")


def insertNode(head, newNode, positionOfNode):
    if positionOfNode == 1:
        newNode.next = head
        return newNode

    currentNode = head
    for _ in range(positionOfNode - 2):
        if currentNode == None:
            break
        currentNode = currentNode.next

    newNode.next = currentNode.next
    currentNode.next = newNode

    return head

def deleteNode(head, nodeToDelete):

    if head == nodeToDelete:
        return head.next

    currentNode = head
    while currentNode.next and currentNode.next != nodeToDelete:
        currentNode = currentNode.next

    if currentNode.next is None:
        return head

    currentNode.next = currentNode.next.next

    return head

print("Before deletion:")
traverseAndPrint(node1)

node1 = deleteNode(node1, node4)

print("\nAfter deletion")
traverseAndPrint(node1)

newNode = Node(97)
node1 = insertNode(node1, newNode, 5)

print("\nAfter inserting")
traverseAndPrint(node1)

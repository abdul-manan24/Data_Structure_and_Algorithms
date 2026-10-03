# Implementation of AVL tree and its methods in python.

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

def getHeight(node):
    if not node:
        return 0
    return node.height

def getBalance(node):
    if not node:
        return 0
    return getHeight(node.left) - getHeight(node.right)

def rotateRight(y):
    print("Rotate right on node", y.data)
    x = y.left
    T2 = x.right
    x.right = y
    y.left = T2
    x.height = 1 + max(getHeight(x.left), getHeight(x.right))
    y.height = 1 + max(getHeight(y.left), getHeight(y.right))
    return x

def rotateLeft(x):
    print("Rotate left on node", x.data)
    y = x.right
    T2 = y.left
    y.left = x
    x.right = T2
    x.height = 1 + max(getHeight(x.left), getHeight(x.right))
    y.height = 1 + max(getHeight(y.left), getHeight(y.right))
    return y

def insert(node, data):
    if not node:
        return TreeNode(data)

    if data < node.data:
        node.left = insert(node.left, data)
    elif data > node.data:
        node.right = insert(node.right, data)

    node.height = 1 + max(getHeight(node.left), getHeight(node.right))
    balance = getBalance(node)

    # Balancing the tree
    # Left Left
    if balance > 1 and getBalance(node.left) >= 0:
        return rotateRight(node)

    # Left Right
    if balance > 1 and getBalance(node.left) < 0:
        node.left = rotateLeft(node.left)
        return rotateRight(node)

    # Right Right
    if balance < -1 and getHeight(node.right) <= 0:
        return rotateLeft(node)

    # Right Left
    if balance < -1 and getHeight(node.right) > 0:
        node.right = rotateRight(node.right)
        return rotateLeft(node)

    return node

def inOrderTraversal(node):
    if node is None:
        return 
    inOrderTraversal(node.left)
    print(node.data, end=", ")
    inOrderTraversal(node.right)

def minValueNode(node):
    currentNode = node
    while currentNode.left is not None:
        currentNode = currentNode.left
    return currentNode

def delete(node, data):
    if not node:
        return node

    if data < node.data:
        node.left = delete(node.left, data)
    elif data > node.data:
        node.right = delete(node.right, data)
    else:
        if node.left is None:
            temp = node.right
            node = None
            return temp
        elif node.right is None:
            temp = node.left
            node = None
            return temp

        temp = minValueNode(node.right)
        node.data = temp.data
        node.right = delete(node.right, temp.data)

    if node is None:
        return node

    node.height = 1 + max(getHeight(node.left), getHeight(node.right))
    balance = getBalance(node)

    if balance > 1 and getBalance(node.left) >= 0:
        return rotateRight(node)
    
    if balance > 1 and getBalance(node.left) < 0:
        node.left = rotateLeft(node.left)
        return rotateRight(node)
    
    if balance < -1 and getBalance(node.right) <= 0:
        return rotateLeft(node)

    if balance < -1 and getBalance(node.right) > 0:
        node.right = rotateRight(node.right)
        return rotateLeft(node)

    return node

root = None
numbers = [78, 25, 13, 76, 3, 4, 10, 21, 15, 19]
for number in numbers:
    root = insert(root, number)

inOrderTraversal(root)
delete(root, 21)
inOrderTraversal(root)
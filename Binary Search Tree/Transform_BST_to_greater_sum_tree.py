class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def transformTreeUtil(root):
    if not root:
        return

    transformTreeUtil(root.right)

    global sum

    sum = sum+root.data

    root.data = sum-root.data

    transformTreeUtil(root.left)


def transformTree(root):
    transformTreeUtil(root)


def printInorder(root):
    if (root == None):
        return

    printInorder(root.left)
    print(root.data, end=" ")
    printInorder(root.right)


sum = 0
root = Node(11)
root.left = Node(2)
root.right = Node(29)
root.left.left = Node(1)
root.left.right = Node(7)
root.right.left = Node(15)
root.right.right = Node(40)
root.right.right.left = Node(35)

printInorder(root)
transformTree(root)
print()
printInorder(root)

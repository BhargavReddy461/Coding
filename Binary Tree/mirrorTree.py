class newNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def mirrorTree(root):
    if not root:
        return

    temp = root

    mirrorTree(root.left)
    mirrorTree(root.right)

    temp = root.left
    root.left = root.right
    root.right = temp


def inOrder(node):

    if (node == None):
        return

    inOrder(node.left)
    print(node.data, end=" ")
    inOrder(node.right)


root = newNode(1)
root.left = newNode(2)
root.right = newNode(3)
root.left.left = newNode(4)
root.left.right = newNode(5)

inOrder(root)
mirrorTree(root)
print()
inOrder(root)

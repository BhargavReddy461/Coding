class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def height(root):
    h = 0
    while root:
        root = root.left
        h += 1
    return h


def completerec(root, h, l=0):

    if not root:
        return True

    if root.left is None and root.right is None:
        return h == l+1

    if root.left is None and root.right is not None:
        return False

    return completerec(root.left, h, l+1) and completerec(root.right, h, l+1)


def completetree(root):
    h = height(root)

    return completerec(root, h)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)

print(completetree(root))

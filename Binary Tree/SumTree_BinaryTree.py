class Node:
    def __init__(self, data):

        self.data = data
        self.right = None
        self.left = None


def isleaf(node):

    if node is None:
        return 0
    if node.left is None and node.right is None:
        return 1
    return 0


def sumTree(root):

    ls = 0
    rs = 0

    if root is None or isleaf(root) == 1:
        return 1

    if sumTree(root.left) != 0 and sumTree(root.right) != 0:

        if root.left is None:
            ls = 0
        elif isleaf(root.left) != 0:
            ls = root.left.data
        else:
            ls = 2*root.left.data

        if root.right is None:
            rs = 0
        elif isleaf(root.right) != 0:
            rs = root.right.data
        else:
            rs = 2*root.right.data

        if root.data == ls+rs:
            return 1
        else:
            return 0
    return 0


root = Node(26)
root.left = Node(10)
root.right = Node(3)
root.left.left = Node(6)
root.left.right = Node(4)
root.right.right = Node(3)

print(sumTree(root))

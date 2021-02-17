class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def left(root):
    if root:
        if root.left:
            print(root.data, end=" ")
            left(root.left)
        elif root.right:
            print(root.data, end=" ")
            left(root.right)


def right(root):
    if root:
        if root.right:
            right(root.right)
            print(root.data, end=" ")

        elif root.left:
            right(root.left)
            print(root.data, end=" ")


def leaves(root):

    if root:
        leaves(root.left)

        if root.left is None and root.right is None:
            print(root.data, end=" ")
        leaves(root.right)


def boundarytraversal(root):
    if root:
        print(root.data, end=" ")

        left(root.left)
        leaves(root.left)
        leaves(root.right)
        right(root.right)


root = Node(20)
root.left = Node(8)
root.left.left = Node(4)
root.left.right = Node(12)
root.left.right.left = Node(10)
root.left.right.right = Node(14)
root.right = Node(22)
root.right.right = Node(25)

boundarytraversal(root)

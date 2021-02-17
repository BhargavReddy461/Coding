class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def preorder(root):

    if root is None:
        return

    stack = []
    stack.append(root)

    while len(stack):
        curr = stack.pop()

        print(curr.data, end=" ")

        if curr.right is not None:
            stack.append(curr.right)
        if curr.left is not None:
            stack.append(curr.left)


root = Node(10)
root.left = Node(8)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(5)
root.right.left = Node(2)
preorder(root)

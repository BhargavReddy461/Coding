class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def inorder(root):
    curr = root
    stack = []

    while True:

        if curr:
            stack.append(curr)
            curr = curr.left

        elif stack:

            curr = stack.pop()
            print(curr.data, end=" ")
            curr = curr.right

        else:
            break


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

inorder(root)

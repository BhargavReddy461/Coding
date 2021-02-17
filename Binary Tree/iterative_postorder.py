class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def postorder(root):

    s = []

    while True:

        while root != None:

            s.append(root)
            s.append(root)
            root = root.left

        if len(s) == 0:
            break

        root = s.pop()

        if len(s) > 0 and s[-1] == root:

            root = root.right
        else:
            print(root.data, end=" ")
            root = None


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

postorder(root)

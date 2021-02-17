class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def printRoute(root, q):
    if not root:
        return

    q.append(root.data)

    if root.left is None and root.right is None:
        print(*q)

    printRoute(root.left, q)
    printRoute(root.right, q)
    q.pop()


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

printRoute(root, [])

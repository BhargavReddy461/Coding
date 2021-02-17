class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def diagonaltraversaliterative(root):
    if not root:
        return

    q = []
    q.append(root)
    q.append(None)

    while len(q) > 0:
        temp = q.pop(0)

        if not temp:

            if len(q) == 0:
                return
            print()
            q.append(None)

        else:

            while temp:
                print(temp.data, end=" ")

                if temp.left:
                    q.append(temp.left)
                temp = temp.right


root = Node(8)
root.left = Node(3)
root.right = Node(10)
root.left.left = Node(1)
root.left.right = Node(6)
root.right.right = Node(14)
root.right.right.left = Node(13)
root.left.right.left = Node(4)
root.left.right.right = Node(7)

diagonaltraversaliterative(root)

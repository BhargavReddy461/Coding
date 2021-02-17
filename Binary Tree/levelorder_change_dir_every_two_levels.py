class newNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def levelorder(root):
    if root is None:
        return

    q = []
    q.append(root)
    q.append(None)
    c = 0
    while len(q) > 1:

        node = q.pop(0)

        if node == None:
            q.append(None)
            print()

        else:

            if node.left is not None:
                q.append(node.left)

            if node.right is not None:
                q.append(node.right)

            print(node.data, end=" ")


root = newNode(1)
root.left = newNode(2)
root.right = newNode(3)
root.left.left = newNode(4)
root.left.right = newNode(5)
root.right.left = newNode(6)
root.right.right = newNode(7)
root.left.left.left = newNode(8)
root.left.left.right = newNode(9)
root.left.right.left = newNode(3)
root.left.right.right = newNode(1)
root.right.left.left = newNode(4)
root.right.left.right = newNode(2)
root.right.right.left = newNode(7)
root.right.right.right = newNode(2)
root.left.right.left.left = newNode(16)
root.left.right.left.right = newNode(17)
root.right.left.right.left = newNode(18)
root.right.right.left.right = newNode(19)

print("Level Order Traversal of binary tree is -")
levelorder(root)

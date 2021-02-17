class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def levelorder(root, key):
    if not root:

        root = Node(key)
        return root

    if key <= root.data:

        root.left = levelorder(root.left, key)

    else:
        root.right = levelorder(root.right, key)

    return root


def constructBst(level, n):

    if n == 0:
        return None

    root = None

    for i in range(n):
        root = levelorder(root, level[i])
    return root


def inorderTraversal(root):
    if (root == None):
        return None

    inorderTraversal(root.left)
    print(root.data, end=" ")
    inorderTraversal(root.right)


level = [7, 4, 12, 3, 6, 8, 1, 5, 10]
n = len(level)
root = constructBst(level, n)

inorderTraversal(root)

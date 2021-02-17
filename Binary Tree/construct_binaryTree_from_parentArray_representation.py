class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def createdNode(parent, i, created, root):

    if created[i] is not None:
        return

    created[i] = Node(i)

    if parent[i] == -1:
        root[0] = created[i]
        return
    if created[parent[i]] is None:
        createdNode(parent, parent[i], created, root)

    p = created[parent[i]]

    if p.left is None:
        p.left = created[i]

    else:
        p.right = created[i]


def buildTree(parent):
    n = len(parent)

    created = [None]*(n)
    root = [None]
    for i in range(n):
        createdNode(parent, i, created, root)
    return root[0]


def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


parent = [-1, 0, 0, 1, 1, 3, 5]
root = buildTree(parent)
inorder(root)

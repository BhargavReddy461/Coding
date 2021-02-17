class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def levelorderconstruction(root, arr, i, n):

    if i < n:
        temp = Node(arr[i])
        root = temp

        root.left = levelorderconstruction(root.left, arr, 2*i+1, n)
        root.right = levelorderconstruction(root.right, arr, 2*i+2, n)

        return root


def levelorder(root):
    if root is None:
        return

    q = []
    q.append(root)
    q.append(None)

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


arr = [1, 2, 3, 4, 5, 6, 6, 6, 6]
n = len(arr)
root = None
root = levelorderconstruction(root, arr, 0, n)

levelorder(root)

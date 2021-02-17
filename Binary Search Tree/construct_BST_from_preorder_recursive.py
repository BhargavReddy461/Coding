INT_MIN = float("-infinity")
INT_MAX = float("infinity")


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def constructTreeUtil(pre, key, preindex, mini, maxi, n):

    if preindex[0] >= n:
        return None

    root = None

    if key > mini and key < maxi:

        root = Node(key)
        preindex[0] += 1

        if preindex[0] < n:
            root.left = constructTreeUtil(
                pre, pre[preindex[0]], preindex, mini, key, n)

        if preindex[0] < n:
            root.right = constructTreeUtil(
                pre, pre[preindex[0]], preindex, key, maxi, n)

    return root


def constructTree(pre):

    preindex = [0]
    n = len(pre)
    return constructTreeUtil(pre, pre[0], preindex, INT_MIN, INT_MAX, n)


def printInorder(node):

    if node is None:
        return
    printInorder(node.left)
    print(node.data, end=" ")
    printInorder(node.right)


pre = [10, 5, 1, 7, 40, 50]


root = constructTree(pre)
printInorder(root)

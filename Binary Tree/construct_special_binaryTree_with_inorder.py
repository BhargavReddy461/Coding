class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def printInorder(node):
    if node == None:
        return

    printInorder(node.left)

    print(node.data, end=" ")

    printInorder(node.right)


def buildtree(inorder, start, end):

    if start > end:
        return None

    i = inorder.index(max(inorder[start:end+1]))

    root = Node(inorder[i])

    if start == end:
        return root

    root.left = buildtree(inorder, start, i-1)
    root.right = buildtree(inorder, i+1, end)

    return root


inorder = [5, 10, 40, 30, 28]
Len = len(inorder)
root = buildtree(inorder, 0, Len - 1)

printInorder(root)

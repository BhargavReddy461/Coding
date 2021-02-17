class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def constructTree(pre, n):

    root = Node(pre[0])
    s = []
    s.append(root)
    i = 1

    while i < n:
        temp = None

        while len(s) and pre[i] > s[-1].data:
            temp = s.pop()

        if temp:

            temp.right = Node(pre[i])
            s.append(temp.right)

        else:
            temp = s[-1]
            temp.left = Node(pre[i])
            s.append(temp.left)

        i = i+1

    return root


def printInorder(node):
    if (node == None):
        return

    printInorder(node.left)
    print(node.data, end=" ")
    printInorder(node.right)


pre = [10, 5, 1, 7, 40, 50]
size = len(pre)
root = constructTree(pre, size)
printInorder(root)

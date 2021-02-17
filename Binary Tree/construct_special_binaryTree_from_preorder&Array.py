class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def constructtreeutil(pre, arr, preindex, n):

    index = preindex[0]

    if index == n:
        return None

    temp = Node(pre[index])
    preindex[0] += 1
    print(preindex)

    if arr[index] == 'N':
        temp.left = constructtreeutil(pre, arr, preindex, n)
        temp.right = constructtreeutil(pre, arr, preindex, n)

    return temp


def constructtree(pre, arr, n):
    preindex = [0]

    return constructtreeutil(pre, arr, preindex, n)


def printInorder(node):
    if node == None:
        return

    printInorder(node.left)

    print(node.data, end=" ")

    printInorder(node.right)


root = None


pre = [10, 30, 20, 5, 15]
arr = ['N', 'N', 'L', 'L', 'L']
n = len(pre)

root = constructtree(pre, arr, n)

printInorder(root)

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def buildtree(inorder, preorder, start, end, mp):

    if start > end:
        return None

    global preindex

    curr = preorder[preindex]
    preindex += 1
    tnode = Node(curr)

    if start == end:
        return tnode

    inindex = mp[curr]

    tnode.left = buildtree(inorder, preorder, start, inindex-1, mp)
    tnode.right = buildtree(inorder, preorder, inindex+1, end, mp)

    return tnode


def buildtreewrap(inorder, preorder, length):
    mp = {}
    global preindex
    for i in range(length):
        mp[inorder[i]] = i

    return buildtree(inorder, preorder, 0, length-1, mp)


def printInorder(root):
    if not root:
        return
    printInorder(root.left)
    print(root.data, end=" ")
    printInorder(root.right)


inorder = ['D', 'B', 'E', 'A', 'F', 'C']
preorder = ['A', 'B', 'D', 'E', 'C', 'F']
length = len(inorder)
preindex = 0

root = buildtreewrap(inorder, preorder, length)
printInorder(root)

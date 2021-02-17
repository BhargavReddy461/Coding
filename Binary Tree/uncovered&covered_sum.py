class newNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def sumtree(root):

    if root == None:
        return 0
    return root.data+sumtree(root.left)+sumtree(root.right)


def left(root):

    if root.left is None and root.right is None:
        return root.data

    if root.left:
        return root.data+left(root.left)
    else:
        return root.data+left(root.right)


def right(root):

    if root.left is None and root.right is None:
        return root.data

    if root.right:
        return root.data+right(root.right)
    else:
        return root.data+right(root.left)


def isSame(leftsum, rightsum, treesum, root):

    if treesum-(leftsum+rightsum-root.data) == leftsum+rightsum-root.data:
        return True
    else:
        return False


root = newNode(8)
root.left = newNode(3)

root.left.left = newNode(1)
root.left.right = newNode(6)
root.left.right.left = newNode(4)
root.left.right.right = newNode(7)

root.right = newNode(10)
root.right.right = newNode(14)
root.right.right.left = newNode(13)


leftsum = left(root)
rightsum = right(root)
treesum = sumtree(root)

print(isSame(leftsum, rightsum, treesum, root))

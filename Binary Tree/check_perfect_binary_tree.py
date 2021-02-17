class newNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def height(root):
    h = 0
    while root:
        root = root.left
        h += 1
    return h


def perfectrec(root, h, l=0):

    if not root:
        return True

    if root.left is None and root.right is None:
        return h == l+1

    if root.left is None or root.right is None:
        return False

    return perfectrec(root.left, h, l+1) and perfectrec(root.right, h, l+1)


def perfecttree(root):
    h = height(root)

    return perfectrec(root, h)


root = newNode(10)

root.left = newNode(20)
root.right = newNode(30)

root.left.left = newNode(40)
root.left.right = newNode(50)
root.right.left = newNode(60)
root.right.right = newNode(70)


print(perfecttree(root))

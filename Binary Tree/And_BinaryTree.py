class newNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def convertTree(root):

    if root == None:
        return

    convertTree(root.left)
    convertTree(root.right)

    if root.left is not None and root.right is not None:
        root.data = root.left.data & root.right.data


def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


root = newNode(0)
root.left = newNode(1)
root.right = newNode(0)
root.left.left = newNode(0)
root.left.right = newNode(1)
root.right.left = newNode(1)
root.right.right = newNode(1)

inorder(root)
print()
convertTree(root)
inorder(root)

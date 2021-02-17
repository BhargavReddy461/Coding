class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, key):

    if not root:
        return Node(key)

    else:
        if root.data == key:
            return root
        elif root.data < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root


def search(root, key):

    if root is None or root.data == key:
        return root

    if root.data < key:
        return search(root.right, key)
    return search(root.left, key)


def deleteNode(root, key):

    if not root:
        return root

    if root.data < key:
        root.right = deleteNode(root.right, key)
        return root

    elif root.data > key:
        root.left = deleteNode(root.left, key)
        return root

    if root.left is None:
        temp = root.right
        root = None
        return temp
    elif root.right is None:
        temp = root.left
        root = None
        return temp
    else:
        succParent = root
        succ = root.right

        while succ.left is not None:
            succParent = succ
            succ = succ.left
        if succParent != root:
            succParent.left = succ.right
        else:
            succParent.right = succ.right

        root.data = succ.data
        succ = None
        return root


def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


root = None
root = insert(root, 50)
root = insert(root, 30)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 70)
root = insert(root, 60)
root = insert(root, 80)
inorder(root)
print()
print(search(root, 80))
inorder(root)
print()
deleteNode(root, 80)
inorder(root)

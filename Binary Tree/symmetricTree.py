class newNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def symmetric(root):

    if not root:
        return True

    if root.left is None and root.right is None:
        return True

    q = []
    q.append(root)
    q.append(root)

    while len(q):
        left = q.pop(0)
        right = q.pop(0)

        if left.data != right.data:
            return False

        if left.left and right.right:
            q.append(left.left)
            q.append(right.right)

        elif left.left or right.right:
            return False

        if left.right and right.left:
            q.append(left.right)
            q.append(right.left)

        elif left.right or right.left:
            return False

    return True


root = newNode(1)
root.left = newNode(2)
root.right = newNode(2)
root.left.left = newNode(3)
root.left.right = newNode(4)
root.right.left = newNode(4)
root.right.right = newNode(3)

print(symmetric(root))

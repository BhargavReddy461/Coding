class getNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def fulltree(root):

    if not root:
        return True

    q = []
    q.append(root)

    while len(q):

        temp = q.pop(0)

        if temp.left is None and temp.right is None:
            continue

        if temp.left is None or temp.right is None:
            return False

        q.append(temp.left)
        q.append(temp.right)

    return True


root = getNode(1)
root.left = getNode(2)
root.right = getNode(3)
root.left.left = getNode(4)
root.left.right = getNode(5)

print(fulltree(root))

class newNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def printoddlevels(root, odd=True):
    if not root:
        return

    if odd:
        print(root.data, end=" ")

    printoddlevels(root.left, not odd)
    printoddlevels(root.right, not odd)


root = newNode(1)
root.left = newNode(2)
root.right = newNode(3)
root.left.left = newNode(4)
root.left.right = newNode(5)
root.right.left = newNode(6)
root.right.right = newNode(7)

root.left.left.left = newNode(8)
root.left.right.left = newNode(9)
root.right.left.left = newNode(10)
root.right.right.left = newNode(11)

root.left.left.right = newNode(12)
root.left.right.right = newNode(13)
root.right.left.right = newNode(14)
root.right.right.right = newNode(15)

root.left.left.left.left = newNode(16)
root.left.right.left.left = newNode(17)
root.right.left.left.left = newNode(18)
root.right.right.left.left = newNode(19)

root.left.left.right.left = newNode(20)
root.left.right.right.left = newNode(21)
root.right.left.right.left = newNode(22)
root.right.right.right.left = newNode(23)

root.left.left.left.right = newNode(24)
root.left.right.left.right = newNode(25)
root.right.left.left.right = newNode(26)
root.right.right.left.right = newNode(27)

root.left.left.right.right = newNode(28)
root.left.right.right.right = newNode(29)
root.right.left.right.right = newNode(30)
root.right.right.right.right = newNode(31)


printoddlevels(root)

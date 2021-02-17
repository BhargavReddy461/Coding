class getNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def countPairs(root1, root2, x):

    if root1 is None or root2 is None:
        return 0

    s1 = []
    s2 = []

    c = 0

    while 1:

        while root1:
            s1.append(root1)
            root1 = root1.left

        while root2:
            s2.append(root2)
            root2 = root2.right

        if not len(s1) or not len(s2):
            break

        t1 = s1[-1]
        t2 = s2[-1]

        if t1.data+t2.data == x:
            c += 1
            s1.pop()
            s2.pop()
            root1 = t1.right
            root2 = t2.left

        elif t1.data+t2.data < x:
            s1.pop()
            root1 = t1.right
        else:
            s2.pop()
            root2 = t2.left

    return c


root1 = getNode(5)
root1.left = getNode(3)
root1.right = getNode(7)
root1.left.left = getNode(2)
root1.left.right = getNode(4)
root1.right.left = getNode(6)
root1.right.right = getNode(8)


root2 = getNode(10)
root2.left = getNode(6)
root2.right = getNode(15)
root2.left.left = getNode(3)
root2.left.right = getNode(8)
root2.right.left = getNode(11)
root2.right.right = getNode(18)

x = 16

print("Pairs = ", countPairs(root1, root2, x))

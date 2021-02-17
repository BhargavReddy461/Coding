class newNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def inRange(root, low, high):
    return root.data >= low and root.data <= high


def subtreesRec(root, min, max, count):
    if not root:
        return True

    l = subtreesRec(root.left, min, max, count)
    r = subtreesRec(root.right, min, max, count)

    if l and r and inRange(root, min, max):
        count[0] += 1

        return True

    return False


def getCount(root, low, high):
    count = [0]
    subtreesRec(root, low, high, count)
    return count


root = newNode(10)
root.left = newNode(5)
root.right = newNode(50)
root.left.left = newNode(1)
root.right.left = newNode(40)
root.right.right = newNode(100)

l = 5
h = 45
print("Count of subtrees in [", l, ", ", h, "] is ", getCount(root, l, h))

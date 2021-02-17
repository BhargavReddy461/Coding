class newNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


Max = 2**31


def checkLeafLevels(root):
    if not root:
        return 1
    q = []
    q.append(root)
    res = Max
    level = 0

    while len(q):
        size = len(q)
        level += 1

        while size > 0 and len(q):

            temp = q.pop(0)

            if temp.left:
                q.append(temp.left)

                if temp.left.left is None and temp.left.right is None:

                    if res == Max:
                        res = level
                    elif res != level:
                        return 0

            if temp.right:
                q.append(temp.right)

                if temp.right.left is None and temp.right.right is None:

                    if res == Max:
                        res = level
                    elif res != level:
                        return 0
            size -= 1
    return 1


root = newNode(1)
root.left = newNode(2)
root.right = newNode(3)
root.left.right = newNode(4)
root.right.left = newNode(5)
root.right.right = newNode(6)


print(checkLeafLevels(root))

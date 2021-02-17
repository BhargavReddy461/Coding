class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def count(root):
    if root == None:
        return 0

    return count(root.left)+1+count(root.right)


def checkrec(root, n):

    global res
    if root == None:
        return 0

    c = checkrec(root.left, n)+1+checkrec(root.right, n)

    if c == n-c:
        res = True

    return c


def check(root):
    n = count(root)

    checkrec(root, n)


res = False
root = Node(5)
root.left = Node(1)
root.right = Node(6)
root.left.left = Node(3)
root.right.left = Node(7)
root.right.right = Node(4)

check(root)
print(res)

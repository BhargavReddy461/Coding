class newNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def toptobottom(curr, parent):
    s = []
    while curr:
        s.append(curr)
        curr = parent[curr]

    s.reverse()
    for i in s:
        print(i.data, end=" ")
    print()


def printRoute(root):

    if not root:
        return

    q = []
    q.append(root)

    parent = {}

    parent[root] = None

    while len(q):

        curr = q.pop()

        if curr.left is None and curr.right is None:
            toptobottom(curr, parent)

        if curr.left:
            q.append(curr.left)
            parent[curr.left] = curr
        if curr.right:
            q.append(curr.right)
            parent[curr.right] = curr


root = newNode(10)
root.left = newNode(8)
root.right = newNode(2)
root.left.left = newNode(3)
root.left.right = newNode(5)
root.right.left = newNode(2)

printRoute(root)

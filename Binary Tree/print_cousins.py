class newNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def printCousins(root, node):

    if not root:
        print("empty tree")
        return

    if root == node:
        print("No cousins,no siblings")
        return None

    if root.right == node or root.left == node:
        print("No cousins,only siblings")
        return None

    q = []
    q.append(root)
    temp = None
    found = False

    while len(q) and not found:
        size = len(q)

        while size:

            temp = q.pop(0)

            if temp.left == node or temp.right == node:
                found = True

            else:
                if temp.left:
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right)

            size -= 1

    if found:

        for i in range(len(q)):
            print(q[i].data, end=" ")
    else:
        print("node not found")


root = newNode(1)
root.left = newNode(2)
root.right = newNode(3)
root.left.left = newNode(4)
root.left.right = newNode(5)
root.left.right.right = newNode(15)
root.right.left = newNode(6)
root.right.right = newNode(7)
root.right.left.right = newNode(8)

x = newNode(43)

printCousins(root, root)
printCousins(root, root.right)
printCousins(root, root.left.right)

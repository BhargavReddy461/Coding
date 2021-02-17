class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def changesubtreesforevenlevel(root1, root2, l):
    if not root1 and not root2:
        return

    if l % 2 == 0:
        temp = root1.data
        root1.data = root2.data
        root2.data = temp

    changesubtreesforevenlevel(root1.left, root2.right, l+1)
    changesubtreesforevenlevel(root1.right, root2.left, l+1)


def reverseAlternate(root):
    changesubtreesforevenlevel(root.left, root.right, 0)


def levelorder(root):
    if root is None:
        return

    q = []
    q.append(root)
    q.append(None)

    while len(q) > 1:

        node = q.pop(0)

        if node == None:
            q.append(None)
            print()

        else:

            if node.left is not None:
                q.append(node.left)

            if node.right is not None:
                q.append(node.right)

            print(node.data, end=" ")


root = Node(1)

root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

root.left.left.left = Node(8)
root.left.left.right = Node(9)
root.left.right.left = Node(10)
root.left.right.right = Node(11)
root.right.left.left = Node(12)
root.right.left.right = Node(13)
root.right.right.left = Node(14)
root.right.right.right = Node(15)

root.left.left.left.left = Node(16)
root.left.left.left.right = Node(17)
root.left.left.right.left = Node(18)
root.left.left.right.right = Node(19)
root.left.right.left.left = Node(20)
root.left.right.left.right = Node(21)
root.left.right.right.left = Node(22)
root.left.right.right.right = Node(23)
root.right.left.left.left = Node(24)
root.right.left.left.right = Node(25)
root.right.left.right.left = Node(26)
root.right.left.right.right = Node(27)
root.right.right.left.left = Node(28)
root.right.right.left.right = Node(29)
root.right.right.right.left = Node(30)
root.right.right.right.right = Node(31)

levelorder(root)
reverseAlternate(root)
print()
levelorder(root)

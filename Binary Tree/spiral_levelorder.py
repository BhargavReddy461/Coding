class newNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def levelorder(root):
    if root is None:
        return

    s1 = []
    s2 = []

    s1.append(root)

    while len(s1) or len(s2):

        while len(s1):
            temp = s1.pop()
            print(temp.data, end=" ")

            if temp.right:
                s2.append(temp.right)
            if temp.left:
                s2.append(temp.left)

        while len(s2):
            temp = s2.pop()
            print(temp.data, end=" ")

            if temp.left:
                s1.append(temp.left)
            if temp.right:
                s1.append(temp.right)


root = newNode(1)
root.left = newNode(2)
root.right = newNode(3)
root.left.left = newNode(7)
root.left.right = newNode(6)
root.right.left = newNode(5)
root.right.right = newNode(4)
levelorder(root)

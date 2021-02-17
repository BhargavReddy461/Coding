class newNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def AreMirror(root1, root2):

    s1 = []
    s2 = []

    while 1:

        while root1 and root2:

            if root1.data != root2.data:
                return "No"

            s1.append(root1)
            s2.append(root2)

            root1 = root1.left
            root2 = root2.right

        if root1 != None and root2 != None:
            return "No"

        if len(s1) != 0 and len(s2) != 0:

            root1 = s1.pop()
            root2 = s2.pop()

            root1 = root1.right

            root2 = root2.left

        else:
            break

    return "Yes"


root1 = newNode(1)  # 1
root1.left = newNode(3)  # / \
root1.right = newNode(2)  # 3    2
root1.right.left = newNode(5)  # / \
root1.right.right = newNode(4)  # 5      4

# 2nd binary tree formation
root2 = newNode(1)  # 1
root2.left = newNode(2)  # / \
root2.right = newNode(3)  # 2     3
root2.left.left = newNode(4)  # / \
root2.left.right = newNode(5)  # 4  5

print(AreMirror(root1, root2))

class newNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def postorder(root):
    temp = root
    vis = set()

    while temp and temp not in vis:

        if temp.left and temp.left not in vis:
            temp = temp.left
        elif temp.right and temp.right not in vis:
            temp = temp.right

        else:

            print(temp.data, end=" ")
            vis.add(temp)
            temp = root


root = newNode(8)
root.left = newNode(3)
root.right = newNode(10)
root.left.left = newNode(1)
root.left.right = newNode(6)
root.left.right.left = newNode(4)
root.left.right.right = newNode(7)
root.right.right = newNode(14)
root.right.right.left = newNode(13)
postorder(root)

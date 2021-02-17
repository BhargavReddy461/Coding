class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def completetree(root):

    if not root:
        return True

    q = []
    q.append(root)

    while len(q):
        temp = q.pop(0)
        flag = False

        if temp.left:

            if flag == True:
                return False

            q.append(temp.left)

        else:
            flag = True

        if temp.right:

            if flag == True:
                return False

            q.append(temp.right)

        else:
            flag = True
    return True


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)

print(completetree(root))

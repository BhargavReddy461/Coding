class newNode:
    def __init__(self, data):

        self.data = data
        self.right = None
        self.left = None


def sumproperty(root):

    left_data = 0
    right_data = 0

    if (root == None or (root.left is None and root.right is None)):

        return 1

    else:

        if root.left != None:
            left_data = root.left.data

        if root.right != None:
            right_data = root.right.data

        if root.data == (left_data+right_data) and sumproperty(root.left) and sumproperty(root.right):
            return 1
        else:
            return 0


root = newNode(10)
root.left = newNode(8)
root.right = newNode(2)
root.left.left = newNode(3)
root.left.right = newNode(5)
root.right.right = newNode(2)

if(sumproperty(root)):
    print("The given tree satisfies the children sum property ")
else:
    print("The given tree does not satisfy the children sum property ")

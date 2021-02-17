# Python3 program to flip
# a binary tree

# A binary tree node
class Node:

    # Constructor to create
    # a new node
    def __init__(self, data):

        self.data = data
        self.right = None
        self.left = None


def flipBinaryTree(root):

    # Base Cases
    if root is None:
        return root

    if (root.left is None and
            root.right is None):
        return root

    # Recursively call the
    # same method
    flippedRoot = flipBinaryTree(root.left)

    # Rearranging main root Node
    # after returning from
    # recursive call
    root.left.left = root.right
    root.left.right = root
    root.left = root.right = None

    return flippedRoot


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


# Driver code
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.right.left = Node(4)
root.right.right = Node(5)


levelorder(root)
print("\n")

root = flipBinaryTree(root)

levelorder(root)

# This code is contributed by Nikhil Kumar Singh(nickzuck_007)

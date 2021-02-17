''' A binary tree node has key, pointer to left
child and a pointer to right child '''


class Node:

    def __init__(self, key):

        self.key = key
        self.left = None
        self.right = None

# To create a newNode of tree and return pointer


def newNode(key):

    temp = Node(key)
    return temp

# Takes two parameters - same initially and
# calls recursively


def printMiddleLevelUtil(a, b):

    # Base case e
    if (a == None or b == None):
        return

    # Fast pointer has reached the leaf so print
    # value at slow pointer
    if ((b.left == None) and (b.right == None)):
        print(a.key, end=' ')

        return

    # Recursive call
    # root.left.left and root.left.right will
    # print same value
    # root.right.left and root.right.right
    # will print same value
    # So we use any one of the condition
    if (b.left.left):
        printMiddleLevelUtil(a.left, b.left.left)
        printMiddleLevelUtil(a.right, b.left.left)

    else:
        printMiddleLevelUtil(a.left, b.left)
        printMiddleLevelUtil(a.right, b.left)

# Main printing method that take a Tree as input


def printMiddleLevel(node):

    printMiddleLevelUtil(node, node)


# Driver program to test above functions
if __name__ == '__main__':

    n1 = newNode(1)
    n2 = newNode(2)
    n3 = newNode(3)
    n4 = newNode(4)
    n5 = newNode(5)
    n6 = newNode(6)
    n7 = newNode(7)

    n2.left = n4
    n2.right = n5
    n3.left = n6
    n3.right = n7
    n1.left = n2
    n1.right = n3

    printMiddleLevel(n1)

# This code is contributed by rutvik_56

# Python 3 Program to check if there
# is a dead end in BST or not.

class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# A utility function to insert a
# new Node with given key in BST


def insert(node, key):

    # If the tree is empty,
    # return a new Node
    if node == None:
        return Node(key)

    # Otherwise, recur down the tree
    if key < node.data:
        node.left = insert(node.left, key)
    elif key > node.data:
        node.right = insert(node.right, key)

    # return the (unchanged) Node pointer
    return node

# Returns true if tree with given
# root contains dead end or not.
# min and max indicate range
# of allowed values for current node.
# Initially these values are full range.


def deadEnd(root, Min, Max):

    # if the root is null or the recursion
    # moves after leaf node it will return
    # false i.e no dead end.
    if root == None:
        return False

    # if this occurs means dead
    # end is present.
    if Min == Max:
        return True

    # heart of the recursion lies here.
    return (deadEnd(root.left, Min, root.data - 1) or
            deadEnd(root.right, root.data + 1, Max))


# Driver Code
if __name__ == '__main__':

    #		 8
    #	 / \
    #	 5 11
    #	 / \
    # 2 7
    #	 \
    #	 3
    #	 \
    #	 4
    root = None
    root = insert(root, 8)
    root = insert(root, 5)
    root = insert(root, 2)
    root = insert(root, 3)
    root = insert(root, 7)
    root = insert(root, 11)
    root = insert(root, 4)
    if deadEnd(root, 1, 9999999999) == True:
        print("Yes")
    else:
        print("No")

# This code is contributed by PranchalK

# Python3 code to find the largest
# value smaller than or equal to N
class newNode:

    # Constructor to create a new node
    def __init__(self, data):
        self.key = data
        self.left = None
        self.right = None

# To insert a new node in BST


def insert(node, key):

    # if tree is empty return new node
    if node == None:
        return newNode(key)

    # if key is less then or grater then
    # node value then recur down the tree
    if key < node.key:
        node.left = insert(node.left, key)
    elif key > node.key:
        node.right = insert(node.right, key)

    # return the (unchanged) node pointer
    return node

# function to find max value less then N


def findMaxforN(root, N):

    # Base cases
    if root == None:
        return -1
    if root.key == N:
        return N

    # If root's value is smaller, try in
    # right subtree
    elif root.key < N:
        k = findMaxforN(root.right, N)
        if k == -1:
            return root.key
        else:
            return k

    # If root's key is greater, return
    # value from left subtree.
    elif root.key > N:
        return findMaxforN(root.left, N)


# Driver code
if __name__ == '__main__':
    N = 4

    # creating following BST
    #
    #			 5
    #		 / \
    #		 2	 12
    #	 / \ / \
    #	 1 3 9 21
    #				 / \
    #			 19 25
    root = None
    root = insert(root, 25)
    insert(root, 2)
    insert(root, 1)
    insert(root, 3)
    insert(root, 12)
    insert(root, 9)
    insert(root, 21)
    insert(root, 19)
    insert(root, 25)
    print(findMaxforN(root, N))

# This code is contributed by PranchalK

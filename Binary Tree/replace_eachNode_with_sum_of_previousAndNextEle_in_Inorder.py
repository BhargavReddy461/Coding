class getNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def inorder(root, arr):

    if not root:
        return

    inorder(root.left, arr)
    arr.append(root.data)
    inorder(root.right, arr)


def inordersum(root, arr, i):

    if not root:
        return

    inordersum(root.left, arr, i)
    root.data = arr[i-1]+arr[i+1]
    i += 1
    inordersum(root.right, arr, i)


def inordersumutil(root):
    if not root:
        return

    arr = []
    arr.append(0)
    inorder(root, arr)
    arr.append(0)

    i = 1
    inordersum(root, arr, i)


def preorderTraversal(root):

    # if root is None
    if (not root):
        return

    # first print the data of node
    print(root.data, end=" ")

    # then recur on left subtree
    preorderTraversal(root.left)

    # now recur on right subtree
    preorderTraversal(root.right)


if __name__ == '__main__':

    # binary tree formation
    root = getNode(1)  # 1
    root.left = getNode(2)  # / \
    root.right = getNode(3)  # 2     3
    root.left.left = getNode(4)  # / \ / \
    root.left.right = getNode(5)  # 4 5 6 7
    root.right.left = getNode(6)
    root.right.right = getNode(7)

    print("Preorder Traversal before",
          "tree modification:")
    preorderTraversal(root)

    inordersumutil(root)
    print()
    print("Preorder Traversal after",
          "tree modification:")
    preorderTraversal(root)

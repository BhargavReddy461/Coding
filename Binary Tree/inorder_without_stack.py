class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def morris_traversal(root):
    curr = root

    while curr:

        if curr.left is None:
            print(curr.data, end=" ")
            curr = curr.right

        else:

            pre = curr.left

            while pre.right is not None and pre.right is not curr:
                pre = pre.right

            if pre.right is None:

                pre.right = curr
                curr = curr.left

            else:

                pre.right = None
                print(curr.data, end=" ")
                curr = curr.right


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

morris_traversal(root)

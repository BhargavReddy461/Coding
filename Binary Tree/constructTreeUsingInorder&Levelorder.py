class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def buildtree(inorder, levelorder, n):
    if inorder:
        node = None
        in_index = 0

        for i in range(n):
            if levelorder[i] in inorder:

                node = Node(levelorder[i])

                in_index = inorder.index(levelorder[i])

                break

        if not inorder:
            return node

        node.left = buildtree(inorder[0:in_index], levelorder, n)

        node.right = buildtree(inorder[in_index+1:], levelorder, n)

        return node


def _inorder(root):
    temp = root
    if(not temp):
        return
    _inorder(temp.left)
    print(temp.data, end=" ")
    _inorder(temp.right)


levelorder = [20, 8, 22, 4, 12, 10, 14]
inorder = [4, 8, 10, 12, 14, 20, 22]

node = buildtree(inorder, levelorder, len(levelorder))
_inorder(node)

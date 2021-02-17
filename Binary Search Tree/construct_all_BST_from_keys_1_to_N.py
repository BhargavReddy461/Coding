class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def constructTrees(start, end):

    list = []

    if start > end:
        list.append(None)

        return list

    for i in range(start, end+1):

        leftsubtree = constructTrees(start, i-1)
        rightsubtree = constructTrees(i+1, end)

        for j in range(len(leftsubtree)):
            left1 = leftsubtree[j]

            for k in range(len(rightsubtree)):
                right1 = rightsubtree[k]

                node = Node(i)
                node.left = left1
                node.right = right1
                list.append(node)

    return list


def preorder(root):

    if (root != None):

        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)


trees = constructTrees(1, 3)

for i in range(len(trees)):
    preorder(trees[i])
    print()

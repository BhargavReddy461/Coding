class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def inorder(root):
    temp = root
    if(not temp):
        return
    inorder(temp.left)
    print(temp.data, end=" ")
    inorder(temp.right)


def constructTree(mat):

    n = len(mat)
    dict = {}

    for i in range(n):
        total = sum(mat[i])

        dict.setdefault(total, []).append(i)

    node = [Node(-1)]*n

    parent = [False]*n
    last = 0

    for key in dict.keys():
        for row in dict.get(key):

            last = row

            node[row] = Node(row)

            if key == 0:
                continue

            for i in range(n):

                if not parent[i] and mat[row][i] == 1:
                    if node[row].left is None:
                        node[row].left = node[i]
                    else:
                        node[row].right = node[i]

                    parent[i] = True

    return node[last]


mat = [[0, 0, 0, 0, 0, 0],
       [1, 0, 0, 0, 1, 0],
       [0, 0, 0, 1, 0, 0],
       [0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0],
       [1, 1, 1, 1, 0, 0]]
root = constructTree(mat)

inorder(root)

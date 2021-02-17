class newnode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def ancestorRec(root, anc):

    global mat, Max

    if root == None:
        return 0

    data = root.data

    for i in range(len(anc)):

        mat[anc[i]][data] = 1

    anc.append(data)

    l = ancestorRec(root.left, anc)
    r = ancestorRec(root.right, anc)

    anc.pop()

    return l+r+1


def ancestorMatrix(root):
    anc = []

    n = ancestorRec(root, anc)

    for i in range(n):
        for j in range(n):
            print(mat[i][j], end=" ")
        print()


Max = 100

mat = [[0]*Max for i in range(Max)]


root = newnode(5)
root.left = newnode(1)
root.right = newnode(2)
root.left.left = newnode(0)
root.left.right = newnode(4)
root.right.left = newnode(3)

ancestorMatrix(root)

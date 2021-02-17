class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def search(arr, x, n):
    for i in range(n):
        if arr[i] == x:
            return i
    return -1


def postorder(In, pre, n):
    root = search(In, pre[0], n)

    if root != 0:
        postorder(In, pre[1:n], root)

    if root != n-1:
        postorder(In[root+1:], pre[root+1:], n-root-1)

    print(pre[0], end=" ")


In = [4, 2, 5, 1, 3, 6]
pre = [1, 2, 4, 5, 3, 6]
n = len(In)

postorder(In, pre, n)

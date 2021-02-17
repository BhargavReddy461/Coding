class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def hasOneChild(pre, n):

    nextDiff = 0
    lastDiff = 0

    for i in range(n-1):

        nextDiff = pre[i]-pre[i+1]
        lastDiff = pre[i]-pre[-1]
        if nextDiff * lastDiff < 0:
            return False
    return True


pre = [8, 3, 5, 7, 6]

print(hasOneChild(pre, len(pre)))

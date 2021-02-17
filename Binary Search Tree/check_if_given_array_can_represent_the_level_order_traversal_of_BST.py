INT_MAX = float('inf')
INT_MIN = float('-inf')


class Node:
    def __init__(self, data, min, max):
        self.data = data
        self.min = min
        self.max = max


def checkArrToLevelOrder(arr, n):
    if n == 0:
        return True

    q = []
    i = 0
    newNode = Node(arr[i], INT_MIN, INT_MAX)

    i += 1
    q.append(newNode)

    while len(q) and i != n:

        temp = q.pop(0)

        if i < n and arr[i] < temp.data and arr[i] > temp.min:
            newNode = Node(arr[i], temp.min, temp.data)
            i += 1
            q.append(newNode)

        if i < n and arr[i] > temp.data and arr[i] < temp.max:
            newNode = Node(arr[i], temp.data, temp.max)
            i += 1
            q.append(newNode)

    if i == n:
        return True

    return False


arr = [7, 4, 12, 3, 6, 8, 1, 5, 10]
n = len(arr)
if checkArrToLevelOrder(arr, n):
    print("Yes")
else:
    print("No")
